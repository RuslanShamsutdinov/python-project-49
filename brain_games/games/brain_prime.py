#!/usr/bin/env python3
import random
import prompt
from brain_games.scripts.brain_games import main
from brain_games.validation import valid


def prime_test():  # poetry run brain-prime
    name = main()
    count = 0
    print('''Answer "yes" if given number is prime. Otherwise answer "no"''')
    while count < 3:
        k = ''
        correct_answer = 'yes'
        random_number = random.randint(0, 50)
        for i in range(2, random_number//2+1):
            if random_number % i == 0:
                correct_answer = 'no'
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if valid(answer, correct_answer, name):
            count += 1
        else:
            count = 0
    print(f"Congratulations, {name}")


if __name__ == '__main__':
    main()