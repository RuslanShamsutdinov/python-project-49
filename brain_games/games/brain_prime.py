from random import randint
import prompt

ANNOTATIONS = """Answer "yes" if given number is prime.
Otherwise answer "no"."""


def get_answers():  # poetry run brain-prime
    correct_answer = 'yes'
    random_number = randint(2, 50)
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            correct_answer = 'no'
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    return answer, correct_answer
