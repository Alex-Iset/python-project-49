import prompt

from random import randint

from brain_games.constants import (
    NUMBER_QUESTIONS
)


def get_random_numbers(
        start_range: int = 1, end_range: int = 100
) -> int:
    """Returns a random numbers"""
    random_number: int = randint(start_range, end_range)
    return random_number


def start_game(data: callable, condition: str):
    """Starts the game"""
    user_name: str = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(condition)
    question_number: int = 1
    while question_number <= NUMBER_QUESTIONS:
        question, answer = data()
        print(f'Question: {question}')
        user_answer: str = prompt.string('Your answer: ')
        if user_answer.lower() == answer:
            print('Correct!')
            question_number += 1
        else:
            return print(f'"{user_answer}" is wrong answer ;(. '
                         f'Correct answer was "{answer}".'
                         f'\nLet\'s try again, {user_name}!')
    print(f'Congratulations, {user_name}!')
