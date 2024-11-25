from brain_games.consts_and_logic.game_logic import (
    start_game, get_random_numbers
)
from brain_games.consts_and_logic.game_constants import (
    CONDITION_GAME_EVEN
)


def is_even(random_number: int) -> bool:
    """Checks the parity of the number and returns a Boolean value"""
    return True if random_number % 2 == 0 else False


def get_random_number_and_check_even() -> tuple[int, str]:
    """Checks the parity of a random number and
    returns it and the result of the check"""
    random_number = get_random_numbers()
    check_even = 'yes' if is_even(random_number) else 'no'
    return random_number, check_even


def game_even():
    """Starts the game"""
    start_game(get_random_number_and_check_even, CONDITION_GAME_EVEN)
