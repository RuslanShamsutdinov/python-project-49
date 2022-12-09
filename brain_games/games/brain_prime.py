from random import randint

ANNOTATION = """Answer "yes" if given number is prime. Otherwise answer "no"."""


def is_prime(random_number):
    divider_count = 0
    if random_number == 2:
        return True
    if random_number in [0, 1]:
        return False
    for i in range(1, random_number // 2 + 1):
        if random_number % i == 0:
            divider_count += 1
    if divider_count > 1:
        return False
    else:
        return True


def get_question_and_correct_answer():
    correct_answer = 'no'
    question = randint(0, 20)
    if is_prime(question):
        correct_answer = 'yes'
    return correct_answer, question
