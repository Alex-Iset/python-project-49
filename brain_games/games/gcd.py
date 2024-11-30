from brain_games.engine import start_game
from brain_games.utils import get_random_numbers
from brain_games.constants import CONDITION_GAME_GCD


def get_random_numbers_and_gcd() -> tuple[str, str]:
    """Returns random numbers and their greatest common divisor"""
    number1, number2 = (
        get_random_numbers(end_range=30),
        get_random_numbers(end_range=30)
    )
    greatest_common_divisor = ''
    for i in range(1, 30):
        if number1 % i == 0 == number2 % i == 0:
            greatest_common_divisor = str(i)
    numbers = f'{number1} {number2}'
    return numbers, greatest_common_divisor


def game_gcd():
    """Starts the game"""
    start_game(get_random_numbers_and_gcd, CONDITION_GAME_GCD)
