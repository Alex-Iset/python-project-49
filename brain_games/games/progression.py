from random import choice

from brain_games.constants import CONDITION_GAME_PROGRESSION
from brain_games.engine import start_game
from brain_games.utils import get_random_numbers


def get_random_index(progression: list[str]) -> int:
    """Returns a random index"""
    random_index = progression.index(choice(progression))
    return random_index


def get_progression_and_correct_answer() -> tuple[str, str]:
    """Returns a progression and the correct answer"""
    start_range, end_range = (
        get_random_numbers(
            start_range=1, end_range=5
        ),
        get_random_numbers(
            start_range=15, end_range=15
        )
    )
    progression = []
    random_multiplier = get_random_numbers(
        start_range=2, end_range=10
    )
    for i in range(start_range, end_range):
        progression.append(str(i * random_multiplier))
    random_index = get_random_index(progression)
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    result_progression = ' '.join(progression)
    return result_progression, correct_answer


def game_progression():
    """Starts the game"""
    start_game(get_progression_and_correct_answer, CONDITION_GAME_PROGRESSION)
