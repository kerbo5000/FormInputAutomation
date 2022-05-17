import bot.constants as const
import os
from selenium import webdriver
from faker import Faker
from faker.providers import internet, company

class FormInput(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(FormInput, self).__init__(options=options)
        self.implicitly_wait(30)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def tabs(self,tab):
        button = self.find_element_by_id(f'{tab}-btn')
        button.click()

    def login(self, username, password):
        username_field = self.find_element_by_css_selector('input[name="login-username"]')
        username_field.send_keys(username)
        password_field = self.find_element_by_css_selector('input[name="login-password"]')
        password_field.send_keys(password)
        submit = self.find_element_by_css_selector('button[name="login-submit"]')
        submit.click()

    def signup(self):
        fake = Faker()
        fake.add_provider(internet)
        email = fake.ascii_company_email()
        email_field = self.find_element_by_css_selector('input[name="signup-email"]')
        email_field.send_keys(email)
        username = fake.user_name();
        username_field = self.find_element_by_css_selector('input[name="signup-username"]')
        username_field.send_keys(username)
        password = fake.iana_id()
        password_field = self.find_element_by_css_selector('input[name="signup-password"]')
        password_field.send_keys(password)
        repeat_password_field = self.find_element_by_css_selector('input[name="signup-repeat-password"]')
        repeat_password_field.send_keys(password)
        submit = self.find_element_by_css_selector('button[name="signup-submit"]')
        submit.click()

    def add_account(self):
        fake = Faker()
        fake.add_provider(internet)
        fake.add_provider(company)
        username = self.find_element_by_id('user').text.split()[-1]
        self.find_element_by_id('add-btn').click()
        account = fake.company()
        account_field = self.find_element_by_css_selector('input[name="account-name"]')
        account_field.send_keys(account)
        email = fake.free_email_domain()
        email_field = self.find_element_by_css_selector('input[name="email"]')
        email_field.send_keys(username+email)
        port = fake.port_number()
        username_field = self.find_element_by_css_selector('input[name="username"]')
        username_field.send_keys(username+str(port))
        password = fake.iana_id()
        password_field = self.find_element_by_css_selector('input[name="password"]')
        password_field.send_keys(password)
        submit = self.find_element_by_css_selector('input[name="submit"]')
        submit.click()
