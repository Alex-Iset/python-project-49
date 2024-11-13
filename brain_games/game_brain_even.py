from random import randint
import prompt


def get_random_number() -> int:
    random_number: int = randint(1, 100)
    return random_number


def get_user_answer() -> str:
    user_answer: str = prompt.string('Your answer: ')
    return user_answer


def get_congratulation(user_name: str) -> str:
    return f'Congratulations, {user_name}!'


def check_user_answer(random_number: int,
                      user_name: str,
                      user_answer: str) -> str:
    if user_answer.lower() == 'yes':
        if random_number % 2 == 0:
            return 'Correct!'
        else:
            return (f"'yes' is wrong answer ;(. "
                    f"Correct answer was 'no'."
                    f"\nLet's try again, {user_name}!")
    elif user_answer.lower() == 'no':
        if random_number % 2 != 0:
            return 'Correct!'
        else:
            return (f"'no' is wrong answer ;(. "
                    f"Correct answer was 'yes'."
                    f"\nLet's try again, {user_name}!")
    else:
        return (f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was 'yes' or 'no'."
                f"\nLet's try again, {user_name}!")


def get_user_answers(check: str, user_name: str) -> str:
    count = 0
    while count < 2:
        if check == 'Correct!':
            count += 1
            print(f'Question: {get_random_number()}')
            get_user_answer()
            print(check)
        else:
            return check
    return get_congratulation(user_name)


def start_game():
    user_name: str = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_number: int = get_random_number()
    print(f'Question: {random_number}')
    user_answer: str = get_user_answer()
    check: str = check_user_answer(random_number, user_name, user_answer)
    user_answers: str = get_user_answers(check, user_name)
    print(user_answers)
