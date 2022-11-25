#!/usr/bin/env python3

import random
import prompt
from brain_games.welcome import main
from brain_games.validation import valid


def parity_check():  # poetry run brain-even
    name = main()
    tries = 3
    print("""Answer "yes" if the number is even, otherwise answer "no".""")
    while tries > 0:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        tries += valid(answer, correct_answer, name, tries)


if __name__ == '__main__':
    main()
