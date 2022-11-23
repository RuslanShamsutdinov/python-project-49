#!/usr/bin/env python3


def valid(answer, correct_answer):
    if correct_answer == answer:
        print("Correct!")
        return True
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.")
        return False


