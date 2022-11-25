#!/usr/bin/env python3
import random
import prompt
from brain_games.welcome import main
from brain_games.validation import valid


def progression_test():  # poetry run brain-progr
    name = main()
    tries = 3
    print("What number is missing in the progression?")
    while tries > 0:
        k = ''
        L = []
        random_start = random.randint(1, 20)
        random_progression = random.randint(1, 5)
        random_len = random.randint(5, 10)
        random_position = random.randint(4, random_len - 1)
        for i in range(random_len):
            L.append(random_start + random_progression * i)
        correct_answer = str(L[random_position])
        L[random_position] = '..'
        for i in L:
            k += str(i) + ' '
        print(f'Question: {k}')
        answer = prompt.string('Your answer: ')
        tries += valid(answer, correct_answer, name, tries)


if __name__ == '__main__':
    main()
