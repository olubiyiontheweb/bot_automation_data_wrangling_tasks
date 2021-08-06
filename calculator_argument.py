import argparse
from typing import Optional


def calculate(action, a, b):
    """ 
    Calculate the result of the action and the two numbers.
    """

    print(f'{action}ing a = {a} and b = {b}')

    if action == 'add':
        return a + b
    elif action == 'subtract':
        return a - b
    elif action == 'multiply':
        return a * b
    elif action == 'divide':
        return a / b


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help='Action to perform',
                        type=str, choices=['add', 'subtract', 'multiply', 'divide'], default='add')
    parser.add_argument("-a", help="first number",
                        type=int, default=1)
    parser.add_argument("-b", help="second number",
                        type=int, default=1)

    args = parser.parse_args()

    print(calculate(args.action, args.a, args.b))
