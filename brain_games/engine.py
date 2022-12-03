import prompt


def valid(answer, correct_answer, name, tries):
    if correct_answer == answer and tries > 1:
        print("Correct!")
        return -1
    elif correct_answer == answer and tries == 1:
        print(f"Congratulations, {name}!")
        return -1
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        return -tries


def game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.ANNOTATION)
    tries = 3
    while tries > 0:
        correct_answer, Question = game.get_question_and_correct_answer()
        print(f'Question: {Question}')
        answer = prompt.string('Your answer: ')
        tries += valid(answer, correct_answer, name, tries)
