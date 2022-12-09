from random import randint

ANNOTATION = """Answer "yes" if given number is prime. Otherwise answer "no"."""


def is_prime(random_number):
    for i in range(2, random_number // 2 + 1):
        if random_number in [0, 1] or random_number % i == 0:
            return False
        else:
            return True


def get_question_and_correct_answer():
    correct_answer = 'no'
    question = randint(0, 20)
    if is_prime(question):
        correct_answer = 'yes'
    return correct_answer, question
