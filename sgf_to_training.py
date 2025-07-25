import os
import numpy as np
from sgfmill import sgf, boards

def sgf_to_training_data(sgf_path, board_size=19):
    with open(sgf_path, 'rb') as f:
        sgf_game = sgf.Sgf_game.from_bytes(f.read())
    board = boards.Board(board_size)
    data = []
    for node in sgf_game.get_main_sequence():
        move = node.get_move()
        if move is None:
            continue
        color, (x, y) = move
        if color is None or x is None or y is None:
            continue
        # Input: current board state (as 0=empty, 1=black, -1=white)
        state = np.zeros((board_size, board_size), dtype=np.int8)
        for row in range(board_size):
            for col in range(board_size):
                c = board.get(row, col)
                if c == 'b':
                    state[row, col] = 1
                elif c == 'w':
                    state[row, col] = -1
        # Target: next move (as (x, y) coordinates)
        data.append((state.copy(), (x, y), color))
        board.play(x, y, color)
    return data

def process_all_sgfs(data_dir='data', board_size=19):
    all_data = []
    for fname in os.listdir(data_dir):
        if fname.endswith('.sgf'):
            path = os.path.join(data_dir, fname)
            all_data.extend(sgf_to_training_data(path, board_size))
    return all_data

if __name__ == '__main__':
    data = process_all_sgfs()
    print(f'Parsed {len(data)} positions from SGF files.')
    # Save as numpy arrays for training
    X = np.stack([d[0] for d in data])
    y = np.array([d[1][0]*19 + d[1][1] for d in data])  # flatten move to 0..360
    np.save('X_train.npy', X)
    np.save('y_train.npy', y)
    print('Saved X_train.npy and y_train.npy') 