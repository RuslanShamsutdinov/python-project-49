#!/usr/bin/env python3

import random
import prompt
from brain_games.scripts.brain_games import main
from brain_games.validation import valid


def parity_check():  # poetry run brain-even
    name = main()
    count = 0
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    while count < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        if valid(answer, correct_answer, name):
            count += 1
        else:
            count = 0
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
