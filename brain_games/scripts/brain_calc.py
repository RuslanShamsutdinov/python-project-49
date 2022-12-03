#!/usr/bin/env python3

from brain_games.engine import game_engine
from brain_games.games import brain_calc


def main():
    return game_engine(brain_calc)


if __name__ == '__main__':
    main()
