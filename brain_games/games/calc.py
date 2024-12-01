from random import choice

from brain_games.engine import start_game
from brain_games.utils import get_random_numbers
from brain_games.constants import CONDITION_GAME_CALC


def get_random_math_sign_and_result(
        number1: int, number2: int
) -> tuple[str, int]:
    """Returns a random math sign and the result
    of the performed operation of two random numbers"""
    return choice([
        ('+', number1 + number2),
        ('-', number1 - number2),
        ('*', number1 * number2)
    ])


def get_math_operation_and_answer() -> tuple[str, str]:
    """Returns a math operation and the answer"""
    number1, number2 = (
        get_random_numbers(end_range=20),
        get_random_numbers(end_range=20)
    )
    sign, answer = get_random_math_sign_and_result(number1, number2)
    math_operation = f'{number1} {sign} {number2}'
    return math_operation, answer


def game_calc():
    """Starts the game"""
    start_game(get_math_operation_and_answer, CONDITION_GAME_CALC)
