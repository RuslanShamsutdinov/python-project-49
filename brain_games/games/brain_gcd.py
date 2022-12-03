from random import randint
from math import gcd

ANNOTATION = """Find the greatest common divisor of given numbers."""


def get_question_and_correct_answer():
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    Question = f'{random_number1} {random_number2}'
    correct_answer = str(gcd(random_number1, random_number2))
    return correct_answer, Question
