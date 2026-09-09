# CLI Quiz Game 🎯

A simple command-line quiz game built with Python. The application displays multiple-choice questions in the terminal, accepts the user's answers, keeps track of their score, and provides feedback at the end.

## Features

* Multiple-choice questions with A, B, C, and D options
* Questions are displayed one at a time
* Randomizes the order of questions using `random.shuffle()`
* Tracks the user's score
* Checks answers using `if` statements
* Uses `for` loops to iterate through questions and choices
* Provides feedback based on the final score:

  * **Excellent**
  * **Good**
  * **Try Again**

## Technologies Used

* Python
* `random` module
* Command Line / Terminal

## How to Run

1. Clone the repository:

```bash
git clone <your-repository-url>
```

2. Navigate into the project:

```bash
cd quiz-app
```

3. Run the application:

```bash
python app.py
```

On Windows, you can also use:

```bash
py app.py
```

## How It Works

The quiz stores each question as a dictionary inside a list.

Each question contains:

* The question text
* Four choices
* The correct answer

The program randomly shuffles the questions, loops through them, displays the available choices, and asks the user to enter their answer.

The score increases whenever the user's answer matches the correct answer.

## Example

```text
What is the capital of Kenya?
A Mombasa
B Nairobi
C Kisumu
D Nakuru

Your answer: B
Correct choice
```

At the end:

```text
Your total score is 6
Excellent
```

## Future Improvements

* Add `try/except` for invalid input
* Add a timer for each question
* Allow users to select quiz categories
* Load questions from a JSON or CSV file
* Allow users to restart the quiz
* Add more questions

## Author

Tony
