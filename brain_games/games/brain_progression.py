from random import randint

ANNOTATION = """What number is missing in the progression?"""


def get_question_and_correct_answer():
    List = []
    random_start = randint(1, 20)
    random_progression = randint(1, 5)
    random_len = randint(6, 11)
    random_position = randint(0, random_len - 1)
    for i in range(random_len):
        List.append(str(random_start + random_progression * i))
    correct_answer = List[random_position]
    List[random_position] = '..'
    Question = ' '.join(List)
    return correct_answer, Question
