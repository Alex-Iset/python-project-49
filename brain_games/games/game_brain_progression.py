from random import choice
from brain_games.consts_and_logic.game_logic import (
    start_game, get_random_numbers
)
from brain_games.consts_and_logic.game_constants import (
    CONDITION_GAME_PROGRESSION
)

def get_answer_and_random_index(
        progression: list[str]
) -> tuple[int, str]:
    """The function returns a random index and the correct answer"""
    random_index = progression.index(choice(progression))
    answer = progression[random_index]
    return random_index, answer


def get_progression_and_answer() -> tuple[str, str]:
    """The function returns a progression and the correct answer"""
    start_range, end_range = (
        get_random_numbers(
        start_range=1,
        end_range=5
    ),
        get_random_numbers(
            start_range=15,
            end_range=15
        )
    )
    progression = []
    random_multiplier = get_random_numbers(
                start_range=2, end_range=10
    )
    for i in range(start_range, end_range):
        progression.append(str(i * random_multiplier))
    random_index, answer = get_answer_and_random_index(progression)
    progression[random_index] = '..'
    result_progr = ' '.join(progression)
    return result_progr, answer


def game_progression():
    """Starts the game"""
    start_game(get_progression_and_answer, CONDITION_GAME_PROGRESSION)
