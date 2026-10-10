# CodeAlpha Python Programming Tasks

A collection of beginner-friendly Python projects completed as part of the CodeAlpha Python Programming internship. Each task is a standalone command-line program that uses only the Python standard library, so no extra installation is needed.

## Projects

| Task | Project | File |
|------|---------|------|
| 1 | Text-Based Hangman | `codealpha_task1.py` |
| 2 | Stock Portfolio Tracker | `codealpha_task2.py` |
| 3 | Basic Rule-Based Chatbot | `codealpha_task3.py` |

---

## Task 1: Text-Based Hangman

A classic word-guessing game played in the terminal. The program picks a random word from a predefined list (`google`, `mango`, `youtube`, `fintech`, `system`), and the player guesses one letter at a time.

**Features**
- Random word selection with the `random` module
- Shows the word with blanks for letters not yet guessed (e.g. `g o o _ _ e`)
- 6 incorrect guesses allowed
- Input validation: only a single alphabetic letter is accepted
- Detects repeated guesses without penalising the player
- Win and game-over messages

**Concepts used:** lists, strings, loops, conditionals, `input()`/`print()`, the `random` module

---

## Task 2: Stock Portfolio Tracker

A simple tool that calculates the total value of a user's stock investments using hardcoded prices.

**Available stocks (USD per share):** Apple ($180), Tesla ($250), Google ($140), Microsoft ($330), Amazon ($130)

**Features**
- The user enters stock names and quantities, and types `done` when finished
- Validates stock names and requires positive whole-number quantities
- Combines quantities if the same stock is entered more than once
- Prints a formatted table with quantity, price, value per stock, and the total investment value
- Optionally saves the report to `portfolio_result.txt`

**Concepts used:** dictionaries, functions, loops, error handling (`try`/`except`), string formatting, file handling

---

## Task 3: Basic Rule-Based Chatbot

A simple chatbot that replies to a few predefined messages using if-elif logic.

| User input | Bot reply |
|------------|-----------|
| `hello` | Hi! |
| `how are you` | I'm fine, thanks! |
| `bye` | Goodbye! (ends the chat) |

Any other input gets a friendly fallback message suggesting what to try. Input is converted to lowercase and trimmed, so `Hello` and `  BYE ` also work.

**Concepts used:** `if-elif-else`, functions, `while` loops, `input()`/`print()`

---

## How to Run

Make sure Python 3 is installed, then run any task from the terminal:

```bash
python codealpha_task1.py   # Hangman
python codealpha_task2.py   # Stock Portfolio Tracker
python codealpha_task3.py   # Chatbot
```

## Requirements

- Python 3.6 or higher
- No external libraries

## Author

Muhammad Rehan Farooq 
Profile: https://github.com/rehanfarooq1911
