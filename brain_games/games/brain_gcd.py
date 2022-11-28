from random import randint
import prompt

ANNOTATION = """Find the greatest common divisor of given numbers."""


def get_answers():  # poetry run brain-gcd
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    print(f'Question: {random_number1} {random_number2}')
    while random_number1 != 0 and random_number2 != 0:
        if random_number1 > random_number2:
            random_number1 = random_number1 % random_number2
        else:
            random_number2 = random_number2 % random_number1
    correct_answer = str(random_number1 + random_number2)
    answer = prompt.string('Your answer: ')
    return answer, correct_answer
