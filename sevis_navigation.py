import time
import os
import config
from selenium.webdriver.support.ui import Select
from generate_automated_browser import MyAutomatedClass


secret_usrnm = os.environ['SEVIS_Username']
secret_pswd = os.environ['SEVIS_Password']

general_student_url = '/sevis/action/eligibility/ViewStudentInfo'
transfer_url = 'eventType=transfer_out_even'
shorten_program_url = 'eventType=shorten_program_event'
school_code_url = '/sevis/action/fmeligibility/SchoolNameSearchReturn'
cpt_url = 'employmentInfoData?employment_business_context=02&fm'
opt_url = 'employmentInfoData?employment_business_context=01&fm'
main_menu_url = '/sevis/action/fmeligibility/MainPageData'

# Instantiate the browser object
browser = MyAutomatedClass().generate_webdriver_instance()


def login_to_sevis():
    """
    An automated workflow for generating a headless browser and the navigating
    to SEVIS and logging in.
    """

    browser.get('https://egov.ice.gov/sevis/action/logoff')

    enter_username = browser.find_element_by_id('username')
    enter_username.send_keys(secret_usrnm)
    time.sleep(0.25)

    enter_pwd = browser.find_element_by_id('password')
    enter_pwd.send_keys(secret_pswd)

    signin = browser.find_element_by_id('submit')
    signin.click()

    cont = browser.find_element_by_id('submitButton')
    cont.click()

    read_and_understand1 = browser.find_element_by_id('submit')
    read_and_understand1.click()

    read_and_understand2 = browser.find_element_by_id('submit')
    read_and_understand2.click()

    list_of_school = browser.find_element_by_partial_link_text \
        ('Listing of Schools')
    list_of_school.click()
    print('\nYou are now logged into SEVIS')


def navigate_home():
    main_menu = browser.find_element_by_xpath \
        ('//a[contains(@href,"' + main_menu_url + '")]')
    main_menu.click()


def log_off():
    print('\nYou have 5 seconds before being logged off...')
    time.sleep(5)
    print('\nGoodbye!')
    time.sleep(1)

    logoff = browser.find_element_by_class_name('Menu')
    logoff.click()


def student_transfer(input_SEVISID, input_TransferDate, input_SchoolCode):
    """
    An automated workflow for generating a headless browser and the navigating
    to a website and logging in.
    """
    try:
        sevis_ID_search = browser.find_element_by_id('sevisIdGlobalSearch')
        sevis_ID_search.send_keys(input_SEVISID)
        time.sleep(0.5)

        search = browser.find_element_by_xpath('//*[@title="Student/EV Search"]')
        search.click()
        time.sleep(0.5)

        get_student = browser.find_element_by_xpath\
        ('//a[contains(@href,"'+ general_student_url +'")]')
        get_student.click()
        time.sleep(0.25)

        click_transfer_url = browser.find_element_by_xpath\
        ('//a[contains(@href,"'+ transfer_url +'")]')
        click_transfer_url.click()
        time.sleep(0.5)

        transfer_date = browser.find_element_by_id\
        ('educationInfoForm.transferReleaseDate')
        transfer_date.send_keys(input_TransferDate)
        click_button = browser.find_element_by_id('bypass_validate.select_school')
        time.sleep(0.5)
        click_button.click()

        school_code_button = browser.find_element_by_id('schoolCodeRadio')
        school_code_button.click()

        school_code = browser.find_element_by_id('searchSchoolCode')
        school_code.send_keys(input_SchoolCode)
        time.sleep(0.25)

        submit = browser.find_element_by_id('submit')
        submit.click()

        get_school_code = browser.find_element_by_xpath\
        ('//a[contains(@href,"'+ school_code_url +'")]')
        get_school_code.click()

        print('\nDoes everything look correct and ready to transfer? (Y/N)')
        user_input = input('')
        if user_input == 'y' or 'Y':

            transfer_student_final = browser.find_element_by_id('submit')
            time.sleep(1)
            transfer_student_final.click()

            return_to_view_record = browser.find_element_by_id('submit')
            return_to_view_record.click()
        else:
            main_menu = browser.find_element_by_xpath \
            ('//a[contains(@href,"'+ main_menu_url +'")]')
            main_menu.click()
            log_off()
    except:
        print('An unknown error occured. Taking you back to the main menu.')
        main_menu = browser.find_element_by_xpath \
            ('//a[contains(@href,"' + main_menu_url + '")]')
        main_menu.click()


def reprint_I20(input_SEVISID, I20_reprint_choice):
    """
    An automated workflow for reprinting an I-20 in SEVIS RTI
    """
    try:
        sevis_ID_search = browser.find_element_by_id('sevisIdGlobalSearch')
        sevis_ID_search.send_keys(input_SEVISID)
        time.sleep(0.5)

        search = browser.find_element_by_xpath('//*[@title="Student/EV Search"]')
        search.click()
        time.sleep(0.5)

        get_student = browser.find_element_by_xpath\
        ('//a[contains(@href,"'+ general_student_url +'")]')
        get_student.click()
        time.sleep(0.25)

        find_reprint_button = browser.find_element_by_id('submitButton')
        find_reprint_button.click()

        select_reprint_reason = Select(browser.find_element_by_id
        ('studentStatusInfoForm.reprintReason'))
        select_reprint_reason.select_by_visible_text(I20_reprint_choice)

        # reprint_I20_button = browser.find_element_by_id('Print')
        # reprint_I20_button.click()

    except:
        print('An unknown error occured. Taking you back to the main menu.')
        main_menu = browser.find_element_by_xpath \
        ('//a[contains(@href,"' + main_menu_url + '")]')
        main_menu.click()


def shorten_student_program(input_SEVISID, input_shorten_program_date):
    """
    An automated workflow for shortening a program end date in SEVIS RTI.
    """
    try:
        sevis_ID_search = browser.find_element_by_id('sevisIdGlobalSearch')
        sevis_ID_search.send_keys(input_SEVISID)
        time.sleep(0.5)

        search = browser.find_element_by_xpath('//*[@title="Student/EV Search"]')
        search.click()
        time.sleep(0.5)

        get_student = browser.find_element_by_xpath \
        ('//a[contains(@href,"' + general_student_url + '")]')
        get_student.click()
        time.sleep(0.25)

        click_shorten_url = browser.find_element_by_xpath \
        ('//a[contains(@href,"'+ shorten_program_url +'")]')
        click_shorten_url.click()
        time.sleep(0.5)

        shorten_date = browser.find_element_by_id \
        ('educationInfoForm.newProgramEndDate')
        shorten_date.send_keys(input_shorten_program_date)

        # click_button = browser.find_element_by_id\
        # ('submit')
        # time.sleep(0.5)
        # click_button.click()

    except:
        print('An unknown error occured. Taking you back to the main menu.')
        main_menu = browser.find_element_by_xpath \
        ('//a[contains(@href,"' + main_menu_url + '")]')
        main_menu.click()


def CPT_employment(input_SEVISID, input_CPT_start, input_CPT_end,
    input_FT_PT, input_CPT_Name, input_CPT_addy1, input_CPT_addy2,
    input_CPT_city, get_CPT_state, input_CPT_zip, CPT_type,
    input_Student_Major):
    """
    An automated workflow for requesting CPT Employement in SEVIS RTI
    """
    try:
        sevis_ID_search = browser.find_element_by_id('sevisIdGlobalSearch')
        sevis_ID_search.send_keys(input_SEVISID)
        time.sleep(0.5)

        search = browser.find_element_by_xpath\
        ('//*[@title="Student/EV Search"]')
        search.click()
        time.sleep(0.5)

        get_student = browser.find_element_by_xpath \
        ('//a[contains(@href,"' + general_student_url + '")]')
        get_student.click()
        time.sleep(0.25)

        click_cpt_url = browser.find_element_by_xpath \
        ('//a[contains(@href,"' + cpt_url + '")]')
        click_cpt_url.click()
        time.sleep(0.5)

        new_cpt = browser.find_element_by_xpath \
        ('//a[contains(@href,"employmentData")]')
        new_cpt.click()
        time.sleep(0.5)

        cpt_start_date = browser.find_element_by_id('employmentStartDate')
        cpt_start_date.send_keys(input_CPT_start)

        cpt_end_date = browser.find_element_by_id('employmentEndDate')
        cpt_end_date.send_keys(input_CPT_end)

        select_CPT_hours = Select(browser.find_element_by_id
        ('timeCode'))
        select_CPT_hours.select_by_visible_text(input_FT_PT)

        cpt_name = browser.find_element_by_id('employerName')
        cpt_name.send_keys(input_CPT_Name)

        cpt_addy1 = browser.find_element_by_id('addressForm.com_addr1')
        cpt_addy1.send_keys(input_CPT_addy1)

        cpt_addy2 = browser.find_element_by_id('addressForm.com_addr2')
        cpt_addy2.send_keys(input_CPT_addy2)

        cpt_city = browser.find_element_by_id('addressForm.com_city')
        cpt_city.send_keys(input_CPT_city)

        select_reprint_reason = Select(browser.find_element_by_id
        ('addressForm.com_state_code'))
        select_reprint_reason.select_by_visible_text(get_CPT_state)

        cpt_zip = browser.find_element_by_id('addressForm.com_postal_code')
        cpt_zip.send_keys(input_CPT_zip)

        cpt_employer_remarks = browser.find_element_by_id('employmentRemark')
        join_course_and_major = (CPT_type + input_Student_Major +'.')
        cpt_employer_remarks.send_keys(join_course_and_major)

        cpt_student_remarks = browser.find_element_by_id('studentRemark')
        cpt_student_remarks.send_keys(join_course_and_major)

        print('\nDoes everything look correct and ready to submit? (Y/N)')
        user_input = input('')
        if user_input == 'Y'.lower():
            cpt_submit_final = browser.find_element_by_id('submit')
            time.sleep(1)
            cpt_submit_final.click()

            return_to_view_record = browser.find_element_by_id('submit')
            return_to_view_record.click()
        else:
            main_menu = browser.find_element_by_xpath \
                ('//a[contains(@href,"' + main_menu_url + '")]')
            main_menu.click()

    except:
        print('An unknown error occured. Taking you back to the main menu.')
        main_menu = browser.find_element_by_xpath \
            ('//a[contains(@href,"' + main_menu_url + '")]')
        main_menu.click()


def OPT_employment(input_SEVISID, input_OPT_type, input_FT_PT,
    input_OPT_start, input_OPT_end, input_Student_Major):
    """
    An automated workflow for requesting OPT Employement in SEVIS RTI
    """
    try:
        sevis_ID_search = browser.find_element_by_id('sevisIdGlobalSearch')
        sevis_ID_search.send_keys(input_SEVISID)
        time.sleep(0.5)

        search = browser.find_element_by_xpath\
        ('//*[@title="Student/EV Search"]')
        search.click()
        time.sleep(0.5)

        get_student = browser.find_element_by_xpath \
        ('//a[contains(@href,"' + general_student_url + '")]')
        get_student.click()
        time.sleep(0.25)

        click_cpt_url = browser.find_element_by_xpath \
        ('//a[contains(@href,"' + opt_url + '")]')
        click_cpt_url.click()
        time.sleep(0.5)

        new_cpt = browser.find_element_by_xpath \
        ('//a[contains(@href,"optEmploymentData")]')
        new_cpt.click()
        time.sleep(0.5)

        try:
            academic_year_met = browser.find_element_by_id\
            ('academicYearMetIndicatorFlag')
            time.sleep(0.5)
            academic_year_met.click()

            select_OPT_type = browser.find_element_by_id('optCode')
            select_OPT_type.send_keys(input_OPT_type)

            select_OPT_FT_PT = browser.find_element_by_id('timeCode')
            select_OPT_FT_PT.send_keys(input_FT_PT)

            opt_start_month = browser.find_element_by_id('employmentStartDate1')
            opt_start_month.send_keys(input_OPT_start[0])

            opt_start_day = browser.find_element_by_id('employmentStartDate2')
            opt_start_day.send_keys(input_OPT_start[1])

            opt_start_year = browser.find_element_by_id('employmentStartDate3')
            opt_start_year.send_keys(input_OPT_start[2])

            opt_end_month = browser.find_element_by_id('employmentEndDate1')
            opt_end_month.send_keys(input_OPT_end[0])

            opt_end_day = browser.find_element_by_id('employmentEndDate2')
            opt_end_day.send_keys(input_OPT_end[1])

            opt_end_year = browser.find_element_by_id('employmentEndDate3')
            opt_end_year.send_keys(input_OPT_end[2])

            opt_employer_remarks = browser.find_element_by_id('employmentRemark')
            opt_employer_statement = ('This Practical Training is in the field of '
            'study for this student,' + input_Student_Major + '. We request 12 '
            'months of OPT to begin on 07/15/2019 or the date of adjudication, '
            'whichever is later.')
            opt_employer_remarks.send_keys(opt_employer_statement)

            print('\nDoes everything look correct and ready to submit? (Y/N)')
            user_input = input('')
            if user_input == 'Y'.lower():
                cpt_submit_final = browser.find_element_by_id('submit')
                time.sleep(1)
                cpt_submit_final.click()

                return_to_view_record = browser.find_element_by_id('submit')
                return_to_view_record.click()
            else:
                main_menu = browser.find_element_by_xpath \
                    ('//a[contains(@href,"' + main_menu_url + '")]')
                main_menu.click()
        except:
            select_OPT_type = browser.find_element_by_id('optCode')
            select_OPT_type.send_keys(input_OPT_type)

            select_OPT_FT_PT = browser.find_element_by_id('timeCode')
            select_OPT_FT_PT.send_keys(input_FT_PT)

            opt_start_month = browser.find_element_by_id('employmentStartDate1')
            opt_start_month.send_keys(input_OPT_start[0])

            opt_start_day = browser.find_element_by_id('employmentStartDate2')
            opt_start_day.send_keys(input_OPT_start[1])

            opt_start_year = browser.find_element_by_id('employmentStartDate3')
            opt_start_year.send_keys(input_OPT_start[2])

            opt_end_month = browser.find_element_by_id('employmentEndDate1')
            opt_end_month.send_keys(input_OPT_end[0])

            opt_end_day = browser.find_element_by_id('employmentEndDate2')
            opt_end_day.send_keys(input_OPT_end[1])

            opt_end_year = browser.find_element_by_id('employmentEndDate3')
            opt_end_year.send_keys(input_OPT_end[2])

            opt_employer_remarks = browser.find_element_by_id(
                'employmentRemark')
            opt_employer_statement = (
                        'This Practical Training is in the field of '
                        'study for this student,' + input_Student_Major + '. We request 12 '
                                                                          'months of OPT to begin on 07/15/2019 or the date of adjudication, '
                                                                          'whichever is later.')
            opt_employer_remarks.send_keys(opt_employer_statement)

            print('\nDoes everything look correct and ready to submit? (Y/N)')
            user_input = input('')
            if user_input == 'Y'.lower():
                cpt_submit_final = browser.find_element_by_id('submit')
                time.sleep(1)
                cpt_submit_final.click()

                return_to_view_record = browser.find_element_by_id('submit')
                return_to_view_record.click()
            else:
                main_menu = browser.find_element_by_xpath \
                    ('//a[contains(@href,"' + main_menu_url + '")]')
                main_menu.click()

    except:
        print('An unknown error occured. Taking you back to the main menu.')
        main_menu = browser.find_element_by_xpath \
            ('//a[contains(@href,"' + main_menu_url + '")]')
        main_menu.click()

