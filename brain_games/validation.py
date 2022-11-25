#!/usr/bin/env python3


def valid(answer, correct_answer, name, tries):
    if correct_answer == answer and tries > 1:
        print("Correct!")
        return -1
    elif correct_answer == answer and tries == 1:
        print(f"Congratulations, {name}")
        return -1
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.")
        print(f'Lets try again, {name}!')
        return -1 * tries
