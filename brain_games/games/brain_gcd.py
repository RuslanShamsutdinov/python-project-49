#!/usr/bin/env python3
import random
import prompt
from brain_games.welcome import main
from brain_games.validation import valid


def gcd_test():  # poetry run brain-gcd
    name = main()
    tries = 3
    print("Find the greatest common divisor of given numbers.")
    while tries > 0:
        random_number1 = random.randint(1, 10)
        random_number2 = random.randint(1, 10)
        print(f'Question: {random_number1} {random_number2}')
        while random_number1 != 0 and random_number2 != 0:
            if random_number1 > random_number2:
                random_number1 = random_number1 % random_number2
            else:
                random_number2 = random_number2 % random_number1
        correct_answer = str(random_number1 + random_number2)
        answer = prompt.string('Your answer: ')
        tries += valid(answer, correct_answer, name, tries)


if __name__ == '__main__':
    main()
