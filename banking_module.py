# -*- coding: utf-8 -*-
"""
@author: zejiran.

Simple Banking System Module.
"""
from random import randint


def odd_multiply(numbers):
    for i in range(1, len(numbers) + 1):
        if i % 2 != 0:
            numbers[i - 1] *= 2
    return numbers


def luhn_algorithm(iin, can):
    str_15_digits = f'{iin}{can}'
    numbers = list(map(lambda x: int(x), str_15_digits))
    odd_by_two = odd_multiply(numbers)
    subtracted = map(lambda x: x - 9 if x > 9 else x, odd_by_two)
    checksum = sum(subtracted)
    control_n = 10 - (checksum % 10)
    return control_n if control_n < 10 else 0


class Account:
    def __init__(self):
        self.card_number = None
        self.pin_code = None
        self.balance = 0

    def generate_card_number(self):
        issuer_identification_number = 400000
        customer_account_number = ''.join(f'{randint(0, 9)}' for _ in range(9))
        checksum = luhn_algorithm(issuer_identification_number, customer_account_number)
        self.card_number = f'{issuer_identification_number}{customer_account_number}{checksum}'

    def generate_pin_code(self):
        self.pin_code = ''.join(f'{randint(0, 9)}' for _ in range(4))

    def auth(self, user_pin):
        return True if self.pin_code == user_pin else False


def new_account_confirmation(account):
    print('\nYour card has been created\n'
          'Your card number:\n'
          f'{account.card_number}\n'
          'Your card PIN:\n'
          f'{account.pin_code}')


def log_into(users):
    user_card = input('\nEnter your card number:\n')
    i = 0
    while i < len(users):
        user = users[i]
        if user.card_number == user_card:
            user_pin = input('Enter your PIN:\n')
            if user.pin_code == user_pin:
                return user
            else:
                return False
        i += 1
    else:
        return False


def show_dashboard():
    print('\n1. Balance\n'
          '2. Log out\n'
          '0. Exit')


def logged_in(user):
    while True:
        show_dashboard()
        user_choice = input('Select an option:\n')
        if user_choice == '1':
            print(f'\nBalance: {user.balance}')
        elif user_choice == '2':
            break
        elif user_choice == '0':
            print('\nBye!')
            exit()
