# -*- coding: utf-8 -*-
"""
@author: zejiran.

Simple Banking System.
"""
import banking_module as md


def show_menu():
    print('\n1. Create an account\n'
          '2. Log into account\n'
          '0. Exit')


def start_banking():
    users = []
    while True:
        show_menu()
        customer_choice = input('Select an option:\n')
        if customer_choice == '1':
            account = md.Account()
            account.generate_card_number()
            account.generate_pin_code()
            md.new_account_confirmation(account)
            users.append(account)
        elif customer_choice == '2':
            is_logged = md.log_into(users)
            if is_logged:
                print('\nYou have successfully logged in!')
                md.logged_in(is_logged)
            else:
                print('\nWrong card number or PIN!')
        elif customer_choice == '0':
            print('\nBye!')
            exit()
        else:
            print('\nPlease select a number from the menu.')


start_banking()
