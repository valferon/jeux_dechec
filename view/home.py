def print_main_menu():
    user_answer = 0
    while user_answer not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        print('Chess tournament')
        print('----------------')
        print('Press 1: To create the tournament')
        print('Press 2: To create a new player')
        print('Press 3: To create match')
        print('Press 4: Save')
        print('Press 5: load')
        print('Press 6: Erase tournaments or players')
        print('Press 7: ')
        print('Press 8: To get reports')
        print('Press 9: To exit')
        user_answer = input('Enter your choice: ')

        return int(user_answer)
