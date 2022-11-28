from random import randint
import prompt

ANNOTATIONS = """What is the result of the expression?"""


def get_answers():  # poetry run brain-calc
    operations = ["+", "-", "*"]
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    random_operation = operations[randint(0, 2)]
    print(f'Question: {random_number1} {random_operation} {random_number2}')
    if random_operation == '+':
        correct_answer = str(random_number1 + random_number2)
    elif random_operation == '-':
        correct_answer = str(random_number1 - random_number2)
    else:
        correct_answer = str(random_number1 * random_number2)
    answer = prompt.string('Your answer: ')
    return answer, correct_answer
