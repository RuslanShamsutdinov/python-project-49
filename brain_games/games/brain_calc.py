#!/usr/bin/env python3
import random
import prompt
from brain_games.welcome import main
from brain_games.validation import valid


def calculator_test():  # poetry run brain-calc
    name = main()
    tries = 3
    operations = ["+", "-", "*"]
    print("What is the result of the expression?")
    while tries > 0:
        random_number1 = random.randint(1, 10)
        random_number2 = random.randint(1, 10)
        random_operation = operations[random.randint(0, 2)]
        print(f'Question: {random_number1} {random_operation} {random_number2}')
        if random_operation == '+':
            correct_answer = str(random_number1 + random_number2)
        elif random_operation == '-':
            correct_answer = str(random_number1 - random_number2)
        else:
            correct_answer = str(random_number1 * random_number2)
        answer = prompt.string('Your answer: ')
        tries += valid(answer, correct_answer, name, tries)


if __name__ == '__main__':
    main()
