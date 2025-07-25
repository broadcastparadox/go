# Go Project (Unified)

**OFFLINE CAPABLE:** This project is fully self-contained. The backend, AI, and all game logic work entirely offline—no internet connection is required for any feature.

This project is a full-stack Go (Baduk/Weiqi) platform with:
- **Backend**: Python (Flask), supports multiple concurrent games, AI vs AI and Player vs AI, and self-play/training.
- **Frontend**: Modern HTML/JS/CSS, supports up to 12 simultaneous games with a beautiful, responsive UI.
- **AI/Training**: Scripts for self-play, training, and model management.

---

## Project Structure

```
Go/
  backend/         # Python backend (Flask API, game logic, AI)
  frontend/        # Static frontend (index.html, go.js, style.css)
  data/            # (Optional) Data files for training or logs
  versions/        # AI model/version files
  ai_data.pkl      # Main AI data file
  selfplay_log.jsonl # Self-play logs
  sgf_to_training.py # SGF training script
```

---

## Requirements

- Python 3.8+
- pip (for backend dependencies)
- Node.js (optional, for static server if you want to serve frontend with npm)

---

## Backend Setup & Run

1. **Install dependencies:**
   ```sh
   cd backend
   pip install flask
   # (or) pip install -r requirements.txt
   ```

2. **Run the backend server:**
   ```sh
   python main.py
   # By default runs on http://localhost:5000
   ```

---

## Frontend Setup & Run

1. **Open `frontend/index.html` directly in your browser**
   - OR serve with a static server (recommended for CORS):
     ```sh
     cd frontend
     python -m http.server 8080
     # or
     npx serve .
     ```
   - Then visit: http://localhost:8080

2. **The frontend will connect to the backend at http://localhost:5000 by default.**

---

## AI & Training Scripts

- **Self-play and training:**
  - `sgf_to_training.py`: Convert SGF files to training data.
  - `selfplay_log.jsonl`: Log of self-play games.
  - `ai_data.pkl`: Main AI data file (used by backend AI).
- **To run training or self-play:**
  - Make sure backend is stopped (to avoid file conflicts).
  - Run the script as needed:
    ```sh
    python sgf_to_training.py
    # (or your own training/self-play scripts)
    ```

---

## Notes

- **Multiple Games:** You can play or watch up to 12 games at once in the frontend.
- **Modes:** Player vs AI and AI vs AI are both supported.
- **AI Data:** The backend uses `ai_data.pkl` for move selection and learning.
- **Logs/Stats:** Use the "View Logs & Stats" button in the frontend for unified logs.
- **Offline Mode:** All backend, AI, and game logic are fully offline. No external APIs or online services are used. You can run and play without any internet connection.

---

## Troubleshooting

- If you see errors about missing modules, double-check your Python environment and install all dependencies.
- If the frontend cannot connect to the backend, ensure both are running and CORS is not blocked (use a static server for the frontend if needed).
- If you update AI data or models, restart the backend to reload them.

---

## License

MIT (or your preferred license) 

## Offline Play Instructions

1. Ensure you have Python 3 and pip installed.
2. Install dependencies:
   ```
   pip install -r backend/requirements.txt
   ```
3. Start the backend server:
   ```
   python backend/main.py
   ```
4. Open your browser and go to [http://localhost:5000/](http://localhost:5000/)
   - The game will run fully offline in your browser.

### One-Click Launch (Windows)

You can use the provided `start_game.bat` file for a one-click launch experience. This will start the backend and open the game in your browser automatically.

No internet connection is required for any part of the game. 