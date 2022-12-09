from random import randint

ANNOTATION = """What is the result of the expression?"""


def get_question_and_correct_answer():
    operations = ["+", "-", "*"]
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    random_operation = operations[randint(0, len(operations) - 1)]
    question = f'{random_number1} {random_operation} {random_number2}'
    if random_operation == '+':
        correct_answer = str(random_number1 + random_number2)
    elif random_operation == '-':
        correct_answer = str(random_number1 - random_number2)
    else:
        correct_answer = str(random_number1 * random_number2)
    return correct_answer, question
