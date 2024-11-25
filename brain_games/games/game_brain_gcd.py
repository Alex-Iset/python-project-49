from brain_games.consts_and_logic.game_logic import (
    start_game, get_random_numbers
)
from brain_games.consts_and_logic.game_constants import (
    CONDITION_GAME_GCD
)


def is_looking_common_division():
    """"""
    number1, number2 = (
        get_random_numbers(end_range=30),
        get_random_numbers(end_range=30)
    )
    result = ''
    for i in range(1, 30):
        if number1 % i == 0 == number2 % i == 0:
            result = str(i)
    numbers = f'{number1}, {number2}'
    return numbers, result



def game_gcd():
    """Starts the game"""
    start_game(is_looking_common_division, CONDITION_GAME_GCD)
