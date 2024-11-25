from brain_games.consts_and_logic.game_logic import (
    start_game, get_random_numbers
)
from brain_games.consts_and_logic.game_constants import (
    CONDITION_GAME_EVEN
)


def is_even_or_odd(random_number: int) -> bool:
    """Checks the parity of the number and returns a Boolean value"""
    return True if random_number % 2 == 0 else False


def get_random_number_and_correct_answer() -> tuple[int, str]:
    """Returns a random number and the correct answer
    depending on whether the number is even or odd"""
    random_number = get_random_numbers()
    correct_answer = 'yes' if is_even_or_odd(random_number) else 'no'
    return random_number, correct_answer


def game_even():
    """Starts the game"""
    start_game(get_random_number_and_correct_answer, CONDITION_GAME_EVEN)
