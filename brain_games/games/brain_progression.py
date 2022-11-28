from random import randint
import prompt

ANNOTATIONS = """What number is missing in the progression?"""


def get_answers():  # poetry run brain-progression
    k = ''
    L = []
    random_start = randint(1, 20)
    random_progression = randint(1, 5)
    random_len = randint(6, 11)
    random_position = randint(0, random_len - 1)
    for i in range(random_len):
        L.append(random_start + random_progression * i)
    correct_answer = str(L[random_position])
    L[random_position] = '..'
    for i in L:
        k += str(i) + ' '
    print(f'Question: {k}')
    answer = prompt.string('Your answer: ')
    return answer, correct_answer
