#!/usr/bin/env python3
import random
import prompt
from brain_games.scripts.brain_games import main
from brain_games.validation import valid


def progression_test():  # poetry run brain-progr
    name = main()
    count = 0
    print("What number is missing in the progression?")
    while count < 3:
        k = ''
        L = []
        random_start = random.randint(1, 20)
        random_progression = random.randint(1, 5)
        random_len = random.randint(5, 10)
        random_position = random.randint(4, random_len - 1)
        for i in range(random_len):
            L.append(random_start + random_progression * i)
        correct_answer = L[random_position]
        L[random_position] = '..'
        for i in L:
            k += str(i) + ' '
        print(f'Question: {k}')
        answer = int(prompt.string('Your answer: '))
        if valid(answer, correct_answer, name):
            count += 1
        else:
            count = 0
    print(f"Congratulations, {name}")


if __name__ == '__main__':
    main()
