# AI Tic-Tac-Toe with Minimax

## Overview

AI Tic-Tac-Toe is a web-based game built using Flask, HTML, CSS, and JavaScript. The application allows a user to play Tic-Tac-Toe against an AI opponent powered by the Minimax algorithm.

The AI evaluates all possible game outcomes and always selects the optimal move, making it impossible to defeat when playing correctly.

---

## Features

* Human vs AI gameplay
* Minimax algorithm implementation
* Optimal AI decision-making
* Win, loss, and draw detection
* Interactive 3×3 game board
* Reset game functionality
* Responsive user interface
* Winning combination highlighting
* Flask backend with API communication

---

## Tech Stack

### Backend

* Python
* Flask

### Frontend

* HTML
* CSS
* JavaScript

### AI Algorithm

* Minimax

---

## How It Works

1. The player makes a move on the game board.
2. The current board state is sent to the Flask backend.
3. The backend passes the board to the Minimax engine.
4. Minimax evaluates all possible future game states.
5. The best move is selected and returned.
6. The AI move is displayed on the board.
7. The game continues until a win or draw is detected.

---

## Project Structure

```text
tic_tac_toe_ai/
│
├── app.py
│
├── minimax/
│   └── ai.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── requirements.txt
│
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Clawstride/tic_tac_toe_ai.git
```

### Navigate to the Project Directory

```bash
cd tic_tac_toe_ai
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```text
http://127.0.0.1:5000
```

---

## Learning Outcomes

Through this project, I practiced:

* Flask web development
* Frontend and backend integration
* REST API communication
* Game state management
* Recursive algorithms
* Decision-making using Minimax
* JavaScript DOM manipulation
* Building complete full-stack applications

---

## Future Improvements

* Difficulty levels
* AI vs AI mode
* Move history tracking
* Scoreboard system
* Dark mode
* Game statistics

---

## Author

**Sanjit Kore**
