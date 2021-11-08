from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():

    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        print(f'Заходим на {self.url}')
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False

        return True

    def is_element_appeared(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.presence_of_element_located((how, what)))
        except (TimeoutException):
            return False

        return True

    def is_element_present_in_element(self, element, how, what):
        try:
            element.find_element(how, what)
        except (NoSuchElementException):
            return False

        return True
