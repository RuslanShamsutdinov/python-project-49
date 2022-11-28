from random import randint
import prompt

ANNOTATIONS = """Answer "yes" if the number is even, otherwise answer "no"."""


def get_answers():  # poetry run brain-even
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    answer = prompt.string('Your answer: ')
    return answer, correct_answer
