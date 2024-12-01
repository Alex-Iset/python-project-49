from math import sqrt

from brain_games.utils import get_random_numbers
from brain_games.constants import CONDITION_GAME_PRIME
from brain_games.engine import start_game


def is_prime(random_number: int) -> bool:
    """Checks if the number is prime and returns a Boolean value"""
    if random_number < 2:
        return False
    for i in range(2, int(sqrt(random_number)) + 1):
        if random_number % i == 0:
            return False
    return True


def get_random_number_and_correct_answer() -> tuple[int, str]:
    """Returns a random number and the correct answer,
    depending on whether this number is prime or not"""
    random_number = get_random_numbers()
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    return random_number, correct_answer


def game_prime():
    """Starts the game"""
    start_game(get_random_number_and_correct_answer, CONDITION_GAME_PRIME)
