#!/usr/bin/env python3


def valid(answer, correct_answer, name):
    if correct_answer == answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.")
        print(f'Lets try again, {name}!')
        return False


