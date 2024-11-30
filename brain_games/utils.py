from random import randint


def get_random_numbers(
        start_range: int = 1, end_range: int = 100
) -> int:
    """Returns a random numbers"""
    random_number: int = randint(start_range, end_range)
    return random_number
