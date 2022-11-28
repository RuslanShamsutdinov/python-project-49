import prompt
from brain_games.validation import valid


def game_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.ANNOTATION)
    tries = 3
    while tries > 0:
        answer, correct_answer = game.get_answers()
        tries += valid(answer, correct_answer, name, tries)
