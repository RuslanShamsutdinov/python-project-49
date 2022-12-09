import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.ANNOTATION)
    round_count = 3
    for i in range(round_count):
        correct_answer, question = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer != answer:
            return print(f"'{answer}' is wrong answer ;(."
                         f"Correct answer was '{correct_answer}'."
                         f"\nLet's try again, {name}!")
        else:
            print("Correct!")
    print(f"Congratulations, {name}!")
