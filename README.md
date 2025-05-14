# Wordle Solver

A Python-based automated solver for the NYT Wordle game that suggests optimal guesses and automatically enters words.

## 🚀 Features

* Automated word entry in Wordle interface
* Optimal word suggestions using minimax strategy
* Manual color pattern input (grey/yellow/green)
* Progress tracking with remaining possible words
* Any word can be used as a starting word ("arise" is used by default)

## 📋 Requirements

* Python 3.x
* Chrome browser
* Python packages:
```
keyboard==0.13.5
PyAutoGUI==0.9.54
pyperclip==1.8.2
Pillow==10.2.0
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/k3vin710/Wordle-Solver.git
cd wordle-solver
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the solver:
```bash
python wordle.py
```

2. Follow the on-screen instructions:
   * Open [Wordle](https://www.nytimes.com/games/wordle/index.html) in Chrome
   * Make sure the game window is visible
   * Close any popups/dialogs
   * Press 'esc' to start

3. For each guess:
   * Wait for the word to be entered automatically
   * Enter the color pattern (0=grey, 1=yellow, 2=green)
   * Program will calculate next optimal guess

## 📁 Project Structure

```
wordle-solver/
├── wordle.py           # Main solver implementation
├── words.py            # Word list handling
├── wordle_words.txt    # Dictionary of possible words
└── requirements.txt    # Python package dependencies
```

## 🔍 How It Works

1. Uses minimax strategy for optimal guesses
2. Starts with "arise" (optimal first word)
3. Updates possible words based on feedback
4. Automated word entry using PyAutoGUI
5. Tracks letter statuses (grey/yellow/green)
6. Narrows down possibilities until solved

## 🤝 Contributing

Contributions welcome! Feel free to submit issues and enhancement requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
