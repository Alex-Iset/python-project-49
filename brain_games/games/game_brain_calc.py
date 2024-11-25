from random import choice

from brain_games.consts_and_logic.game_logic import (
    start_game, get_random_numbers
)
from brain_games.consts_and_logic.game_constants import (
    CONDITION_GAME_CALC
)


def get_random_operation_and_result() -> tuple[str, str]:
    """Returns a random arithmetic operation and
    the result of its calculation"""
    number1, number2 = (
        get_random_numbers(end_range=20),
        get_random_numbers(end_range=20)
    )
    random_operation = choice(
        [
            f'{number1} + {number2}',
            f'{number1} - {number2}',
            f'{number1} * {number2}'
        ]
    )
    split_operation = random_operation.split()
    if '+' in split_operation:
        result = str(int(split_operation[0]) + int(split_operation[2]))
    elif '-' in split_operation:
        result = str(int(split_operation[0]) - int(split_operation[2]))
    else:
        result = str(int(split_operation[0]) * int(split_operation[2]))

    return random_operation, result


def game_calc():
    """Starts the game"""
    start_game(get_random_operation_and_result, CONDITION_GAME_CALC)
