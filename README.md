# ET574-M-HW4-Md-Mahfuzur-Rashid
# ET574 Homework 4: Dice Game Simulator

Name: Md Mahfuzur Rashid
Section: M

## Project Description

This Python console game uses two six-sided dice and object-oriented
programming. The player can play multiple rounds or exit.

## Game Rules

- Total 7 or 11: Win
- Total 2, 3, or 12: Lose
- Total 4, 5, 6, 8, 9, or 10: Roll Again

## Files

- main.py: Die class, DiceGame class, and console menu.
- test_dicegame.py: Seven provided tests and three additional tests.

## How to Run

Start the game:

    python main.py

Run the tests:

    python -m unittest -v test_dicegame

## AI Usage Documentation

### AI Tool and Purpose

I used ChatGPT for step-by-step guidance, code suggestions,
troubleshooting indentation errors, and help adding unit tests.
ChatGPT also helped draft this README.

### Representative Prompts

- "What do u understand?" with the assignment screenshots.
- "Tell me what to do step by step."
- Screenshots of errors and test output to request feedback.

### Evaluation and Modifications

I checked the suggested game rules against the assignment.
The constructor uses sides=6 to match the provided starter tests.
During implementation, I corrected indentation in the DiceGame class,
play_round method, and main function.

I ran the program and checked playing a round, invalid input, and exiting.
I also ran the unit tests and checked the expected results.

## Additional Test Cases

I kept all seven provided tests and added these three tests:

1. test_play_round_win:
   Dice values 3 and 4 must return (3, 4, 7, "Win").

2. test_play_round_lose:
   Dice values 6 and 6 must return (6, 6, 12, "Lose").

3. test_play_round_roll_again:
   Dice values 2 and 3 must return (2, 3, 5, "Roll Again").

These tests use unittest.mock.patch.object to temporarily control
each die's roll result. This makes the expected output predictable
and checks that play_round correctly combines the dice values,
total, and outcome.

## Reflection on AI Use

### 1. How was AI used during development?

ChatGPT provided code suggestions and guidance for the classes,
console menu, Git commands, and additional tests. It also helped
identify indentation errors from screenshots.

### 2. What test scenarios did AI suggest, and which were used?

ChatGPT suggested controlled dice rolls for Win, Lose, and Roll Again.
I added all three scenarios. No suggested test scenarios were rejected.

### 3. What modifications were made to the tests, and why?

I added the patch import and three new test methods while keeping
the provided tests. The new tests check complete round results
with fixed dice values instead of relying on random outcomes.

### 4. How were the test results verified?

I ran python -m unittest -v test_dicegame in Codespaces.
The output showed 10 tests and OK. I also manually checked the
console menu by entering 1 to play, 3 for invalid input, and 2 to exit.

### 5. What did you learn?

I learned that unit tests compare actual results with expected results.
Controlling random values makes specific game outcomes easier to test.
I also learned that Python indentation defines code blocks and that
AI suggestions need to be checked by reading and running the code.