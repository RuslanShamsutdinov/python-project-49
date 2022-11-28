#!/usr/bin/env python3

from brain_games.engine import game_engine
from brain_games.games import brain_gcd


def main():  # poetry run brain-even
    return game_engine(brain_gcd)


if __name__ == '__main__':
    main()
