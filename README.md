# Python Question and Answer Game

This is a simple Python question and answer game designed to help improve your understanding of Python and basic programming concepts like loops, conditionals, and data structures.

## Description

The game asks a series of questions, each with multiple choice answers. The user selects an answer, and the game keeps track of their score. At the end of the game, the user's total score is displayed.

## How It Works

1. A list of questions is stored in a dictionary format, each containing:
   - The question.
   - A set of options.
   - The correct answer (given as the index of the correct option).

2. The user is prompted to select an answer for each question.

3. The game checks the user's answer against the correct one and updates their score.

4. The final score is displayed after all questions have been answered.

### Example Question Format

```python
{
    "question": "Which of these is not a renewable energy source?",
    "options": ["Solar", "Wind", "Coal", "Hydroelectric"],
    "answer": "3"
}
Example Output
Which of these is not a renewable energy source?
1. Solar
2. Wind
3. Coal
4. Hydroelectric

Choose 1/2/3/4: 3
Correct! Score: 1/10
Game Flow
The game will:

Display the question and options.
Ask the user to select an option (1/2/3/4).
Inform the user whether they answered correctly and show the current score.
Repeat until all questions have been answered.
Display the final score at the end.
Getting Started
To run this game on your machine:

Clone the repository:

bash
git clone https://github.com/NnannaMari09033/python_quiz.git
Run the Python script:

bash
python game.py
Contribution
Feel free to contribute to this project, whether it's by improving the code, adding more questions, or enhancing the functionality. Any contributions are welcome!

This project was inspired by how my instructor taught me during my learning journey.

Author
Name: Mari Nnanna
Email: nnannamari@gmail.com
