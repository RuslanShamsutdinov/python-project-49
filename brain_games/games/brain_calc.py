#!/usr/bin/env python3
import random
import prompt
from brain_games.scripts.brain_games import main
from brain_games.validation import valid


def calculator_test(): # poetry run brain-calc
    name = main()
    count = 0
    operations = ["+", "-"]
    print("What is the result of the expression?")
    while count < 3:
        random_number1 = random.randint(1, 10)
        random_number2 = random.randint(1, 10)
        random_operation = operations[random.randint(0, 1)]
        print(f'Question: {random_number1} {random_operation} {random_number2}')
        if random_operation == '+':
            correct_answer = random_number1 + random_number2
        else:
            correct_answer = random_number1 - random_number2
        answer = int(prompt.string('Your answer: '))
        if valid(answer, correct_answer):
            count += 1
        else:
            count = 0
    print(f"Congratulations, {name}")


if __name__ == '__main__':
    main()
