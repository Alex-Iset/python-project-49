from random import randint
import prompt


def get_random_number() -> int:
    """Returns a random number in the range from 1 to 100"""
    start_range = 1
    end_range = 100
    random_number: int = randint(start_range, end_range)
    return random_number


def get_user_answer() -> str:
    """Returns the user's response"""
    user_answer: str = prompt.string('Your answer: ')
    return user_answer


def get_congratulation(user_name: str) -> str:
    """Congratulates the user"""
    congratulation = f'Congratulations, {user_name}!'
    return congratulation


def check_user_answer(random_number: int,
                      user_name: str,
                      user_answer: str) -> str:
    """Checks the user's response"""
    if user_answer.lower() == 'yes':
        if random_number % 2 == 0:
            return 'Correct!'
        else:
            return (f'"yes" is wrong answer ;(. '
                    f'Correct answer was "no".'
                    f'\nLet\'s try again, {user_name}!')
    elif user_answer.lower() == 'no':
        if random_number % 2 != 0:
            return 'Correct!'
        else:
            return (f'"no" is wrong answer ;(. '
                    f'Correct answer was "yes".'
                    f'\nLet\'s try again, {user_name}!')
    else:
        return (f'"{user_answer}" is wrong answer ;(. '
                f'Correct answer was "yes" or "no".'
                f'\nLet\'s try again, {user_name}!')


def start_game():
    """Starts the game"""
    user_name: str = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    number_questions = 3
    while count < number_questions:
        random_number: int = get_random_number()
        print(f'Question: {random_number}')
        user_answer: str = get_user_answer()
        check: str = check_user_answer(random_number, user_name, user_answer)
        if check == 'Correct!':
            count += 1
            print(check)
        else:
            return print(check)
    print(get_congratulation(user_name))
