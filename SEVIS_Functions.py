import menu_selection_options as options


def input_SEVISID():
    user_input = input\
    ("\nPlease input the SEVIS ID for the student you'd like to navigate " 
    "\nType 'q' to quit" 
    "\n\nSEVIS ID: ")
    return user_input


def input_TransferDate():
    user_input = input\
    ("Please input the requested Transfer Date (mm/dd/yyyy): ")
    return user_input


def input_SchoolCode():
    user_input = input\
    ("Please input the SEVIS School Code: ")
    return user_input


def input_shorten_program_date():
    user_input = input\
    ("Please input the new Program End Date (mm/dd/yyyy): ")
    return user_input


def input_CPT_start():
    user_input = input\
    ("Please input the CPT Start Date: ")
    return user_input


def input_CPT_end():
    user_input = input\
    ("Please input the CPT End Date: ")
    return user_input


def input_FT_PT():
    user_input = input(options.FT_PT_CHOICE)
    if user_input == 'F'.lower():
        return 'FULL TIME'
    elif user_input == 'P'.lower():
        return 'PART TIME'


def input_CPT_Name():
    user_input = input\
    ("Please input the CPT Employer Name: ")
    return user_input.title()


def input_CPT_addy1():
    user_input = input\
    ("Please input the CPT Address Line 1: ")
    return user_input.title()


def input_CPT_addy2():
    user_input = input\
    ("Please input the CPT Address Line 2: ")
    return user_input.title()


def input_CPT_city():
    user_input = input\
    ("Please input the CPT City: ")
    return user_input.title()


def get_CPT_state(states_list):
    state = input('\nPlease input the state (i.e. CA): ')
    for x in states_list.keys():
        if x == state.upper():
            return states_list[x]


def input_CPT_Zip():
    user_input = input\
    ("Please input the CPT Zip: ")
    return user_input


def input_CPT_type():
    user_input = input(options.CPT_TYPE_CHOICE)
    if user_input == 'M'.lower():
        return 'Major requirement in '
    elif user_input == 'C'.lower():
        return 'Course requirement in '


def input_Student_Major():
    user_input = input\
    ("Please input the student's major: ")
    return user_input.title()


def I20_reprint_choice():
    user_input = input(options.I20_REPRINT_REASON)
    if user_input == 'D'.lower():
        return 'DAMAGED'
    elif user_input == 'L'.lower():
        return 'LOST'
    elif user_input == 'S'.lower():
        return 'STOLEN'
    elif user_input == 'T'.lower():
        return 'TRAVEL'
    elif user_input == 'U'.lower():
        return 'UPDATED'
    elif user_input == 'N'.lower():
        return 'Updated Form I-20 or Name Conversion'


def input_OPT_type():
    user_input = input(options.PRE_POST_OPT)
    if user_input == 'Pre'.lower():
        return 'Pre Completion'
    elif user_input == 'Post'.lower():
        return 'Post Completion'


def input_OPT_start():
    start_date = input\
    ("Please input the OPT Start Date: ")
    month, day, year = start_date.split('/')
    return month, day, year


def input_OPT_end():
    end_date = input\
    ("Please input the OPT End Date: ")
    month, day, year = end_date.split('/')
    return month, day, year

