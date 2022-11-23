#!/usr/bin/env python3
import random
import prompt
from brain_games.scripts.brain_games import main


def calculator_test():
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
            answer = prompt.string('Your answer: ')
            if correct_answer == int(answer):
                print("Correct!")
                count += 1
            else:
                print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.""")
                count = 0
        if random_operation == '-':
            correct_answer = random_number1 - random_number2
            answer = prompt.string('Your answer: ')
            if correct_answer == int(answer):
                print("Correct!")
                count += 1
            else:
                print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.""")
                count = 0
        if count == 3:
            print(f"Congratulations, {name}")


if __name__ == '__main__':
    main()
