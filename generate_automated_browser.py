from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class MyAutomatedClass():
    """Class to setup a browser"""

    @classmethod
    def generate_webdriver_instance(cls):
        """
        Function generates a webdriver instance and then returns this instance
        to be passed to other functions
        """
        opts = Options()
        browser = Chrome(options=opts)

        return browser

