# High-Low Game

A simple web-based High-Low number guessing game built using Flask, HTML, CSS, and JavaScript.

Players are given a random number and must guess whether it is higher or lower than the computer's number.

---

## Features

- Web-based interactive gameplay
- Choose number of rounds (1–15)
- Live score tracking
- Game over state handling
- Responsive and clean UI
- Flask backend
- Deployable on Render/Railway

---

## Project Structure

```text
highlow-game/
│
├── app.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/kvishwa-dev/High-Low-Game.git
```

---

### 2. Move Into Project Folder

```bash
cd High-Low-Game
```

---

### 3. Create Virtual Environment (Optional but Recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the Flask Server

```bash
python app.py
```

---

### 6. Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

---

## Requirements

- Python 3.8+
- Flask
- Gunicorn

---

## Deployment

Recommended platforms:

- Render
- Railway

### Start Command

```bash
gunicorn app:app
```

---

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript

---

## Future Improvements

- Restart game button
- Leaderboard
- User authentication
- Multiplayer support
- Difficulty modes
- Animations and sound effects

---

## Author

Made with ❤️ by kvishwa-dev