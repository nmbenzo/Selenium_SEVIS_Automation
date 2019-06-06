import menu_selection_options as options
import sevis_navigation as sevis_func
import SEVIS_Functions as func
from states_dict import state_list

main_menu = options.SEVIS_MENU_CHOICES

class Menu:
    """
        This class organizes the various menu options into methods and where the
        global_menu option is returned as an class attribute in each method
        """

    def __init__(self, main_menu):
        """Initializes the global_menu parameter"""
        self.main_menu = main_menu


    def login(self):
        """Uses the existing browser instance to login to SEVIS RTI"""
        sevis_func.login_to_sevis()
        return main_menu


    def navigate_to_home(self):
        """Navigates back to the home screen in SEVIS"""
        sevis_func.navigate_home()
        return main_menu


    def log_out(self):
        """Logs out of the SEVIS system and ends the driver instance"""
        sevis_func.log_off()


    def transfer_student(self):
        """Runs the SEVIS Transfer function"""
        sevis_func.student_transfer(func.input_SEVISID(),
        func.input_TransferDate(), func.input_SchoolCode())
        return main_menu



    def reprint_i20(self):
        """Runs the SEVIS I-20 reprint function"""
        sevis_func.reprint_I20(func.input_SEVISID(),
        func.I20_reprint_choice())
        return main_menu


    def shorten_program(self):
        """Runs the Shorten Program function"""
        sevis_func.shorten_student_program(func.input_SEVISID(),
        func.input_shorten_program_date())
        return main_menu


    def cpt_employment(self):
        """Runs the CPT function"""
        sevis_func.CPT_employment(func.input_SEVISID(), func.input_CPT_start(),
        func.input_CPT_end(), func.input_FT_PT(), func.input_CPT_Name(),
        func.input_CPT_addy1(), func.input_CPT_addy2(), func.input_CPT_city(),
        func.get_CPT_state(state_list), func.input_CPT_Zip(),
        func.input_CPT_type(), func.input_Student_Major())
        return main_menu


    def opt_employment(self):
        """Runs the OPT function"""
        sevis_func.OPT_employment(func.input_SEVISID(), func.input_OPT_type(),
        func.input_FT_PT(),func.input_OPT_start(), func.input_OPT_end(),
        func.input_Student_Major())
        return main_menu
