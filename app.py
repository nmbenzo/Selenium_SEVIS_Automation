from menus import Menu, main_menu


def main():
    """
    Master menu that allows users to select which function they'd like to run
    """
    menu_instance = Menu(main_menu)
    user_input = input(main_menu)
    while user_input != 'q'.lower():
        if user_input == 'L'.lower():
            menu_instance.login()
        elif user_input == 'T'.lower():
            menu_instance.transfer_student()
        elif user_input == 'H'.lower():
            menu_instance.navigate_to_home()
        elif user_input == 'E'.lower():
            menu_instance.log_out()
        elif user_input == 'R'.lower():
            menu_instance.reprint_i20()
        elif user_input == 'S'.lower():
            menu_instance.shorten_program()
        elif user_input == 'C'.lower():
            menu_instance.cpt_employment()
        elif user_input == 'O'.lower():
            menu_instance.opt_employment()

        print('\n')
        menu_again = input('Would you like to see the menu again? (Y/N): ')
        if menu_again == 'Y'.lower():
            user_input = input(main_menu)
        elif menu_again == 'N'.lower():
            break
        else:
            print('Unknown command.')
            user_input = input(main_menu)


if __name__ == '__main__':
    main()