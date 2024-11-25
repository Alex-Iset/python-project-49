from random import choice

from brain_games.consts_and_logic.game_logic import (
    start_game, get_random_numbers
)
from brain_games.consts_and_logic.game_constants import (
    CONDITION_GAME_CALC
)


def get_random_operation(
        random_number1: int, random_number2: int
) -> str:
    """Returns a random arithmetic operation"""
    random_operation = choice(
        [
            f'{random_number1} + {random_number2}',
            f'{random_number1} - {random_number2}',
            f'{random_number1} * {random_number2}'
        ]
    )
    return random_operation


def get_random_operation_and_result() -> tuple[str, str]:
    """Returns a random arithmetic operation and
    the result of its calculation"""
    number1, number2 = (
        get_random_numbers(end_range=20),
        get_random_numbers(end_range=20)
    )
    random_operation = get_random_operation(number1, number2)
    split_random_operation = random_operation.split()
    if '+' in split_random_operation:
        result = str(int(split_random_operation[0]) + int(split_random_operation[2]))
    elif '-' in split_random_operation:
        result = str(int(split_random_operation[0]) - int(split_random_operation[2]))
    else:
        result = str(int(split_random_operation[0]) * int(split_random_operation[2]))

    return random_operation, result


def game_calc():
    """Starts the game"""
    start_game(get_random_operation_and_result, CONDITION_GAME_CALC)
