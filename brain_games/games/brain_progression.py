from random import randint

ANNOTATION = """What number is missing in the progression?"""


def get_question_and_correct_answer():
    progression = []
    random_start = randint(1, 20)
    random_progression_step = randint(1, 5)
    random_len = randint(6, 11)
    random_position = randint(0, random_len - 1)
    for i in range(random_len):
        progression.append(str(random_start + random_progression_step * i))
    correct_answer = progression[random_position]
    progression[random_position] = '..'
    question = ' '.join(progression)
    return correct_answer, question
