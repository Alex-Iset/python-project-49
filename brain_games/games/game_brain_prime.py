from brain_games.consts_and_logic.game_logic import (
    start_game, get_random_numbers
)
from brain_games.consts_and_logic.game_constants import (
    CONDITION_GAME_PRIME
)


def is_prime(random_number) -> bool:
    """Checks if the number is prime and returns a Boolean value"""
    prime_numbers = [1, random_number]
    result = []
    for i in range(1, random_number + 1):
        if random_number % i == 0:
            result.append(i)
    return True if result == prime_numbers else False


def get_random_number_and_check_prime() -> tuple[int, str]:
    """Checks whether a random number is prime and
    returns it along with the result of the check"""
    random_number = get_random_numbers()
    check_prime = 'yes' if is_prime(random_number) else 'no'
    return random_number, check_prime


def game_prime():
    """Starts the game"""
    start_game(get_random_number_and_check_prime, CONDITION_GAME_PRIME)