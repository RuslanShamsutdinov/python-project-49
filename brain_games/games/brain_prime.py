from random import randint

ANNOTATION = """Answer "yes" if given number is prime. Otherwise answer "no"."""


def is_prime(random_number):
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            return True


def get_question_and_correct_answer():
    correct_answer = 'yes'
    Question = randint(2, 50)
    if is_prime(Question):
        correct_answer = 'no'
    return correct_answer, Question


if __name__ == '__main__':
    is_prime()
