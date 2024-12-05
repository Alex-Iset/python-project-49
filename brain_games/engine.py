import prompt

from brain_games.constants import NUMBER_QUESTIONS


def start_game(data: callable, condition: str):
    """Starts the game"""
    user_name = prompt.string(
        'Welcome to the Brain Games!'
        '\nMay I have your name? '
    )
    print(f'Hello, {user_name}!'
          f'\n{condition}')

    for _ in range(NUMBER_QUESTIONS):
        question, answer = data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lower() == str(answer):
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{answer}".'
                  f'\nLet\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')
