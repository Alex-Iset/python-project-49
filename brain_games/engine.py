import prompt

from brain_games.constants import (
    NUMBER_QUESTIONS
)


def start_game(data: callable, condition: str):
    """Starts the game"""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!'
          f'\n{condition}')

    for _ in range(NUMBER_QUESTIONS):
        question, answer = data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() == str(answer):
            print('Correct!')
        else:
            return print(f'"{user_answer}" is wrong answer ;(. '
                         f'Correct answer was "{answer}".'
                         f'\nLet\'s try again, {user_name}!')
    print(f'Congratulations, {user_name}!')
