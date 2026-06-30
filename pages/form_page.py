import logging


class FormPage:

    def __init__(self, page):
        self.page = page

        self.firstname = page.locator('[id="customer.firstName"]')
        self.lastname = page.locator('[id="customer.lastName"]')
        self.address = page.locator('[id="customer.address.street"]')
        self.city = page.locator('[id="customer.address.city"]')
        self.state = page.locator('[id="customer.address.state"]')
        self.zipcode = page.locator('[id="customer.address.zipCode"]')
        self.phonenumber = page.locator('[id="customer.phoneNumber"]')
        self.ssn = page.locator('[id="customer.ssn"]')
        self.username = page.locator('[id="customer.username"]')
        self.password = page.locator('[id="customer.password"]')
        self.confirmpassword = page.locator("#repeatedPassword")
        self.button = page.get_by_role("button", name="Register")

    def navigate(self):
        logging.info("Navigating to ParaBank registration page")
        self.page.goto("https://parabank.parasoft.com/parabank/register.htm")

    def register_firstname(self, firstname):
        logging.info(f"Entering first name: {firstname}")
        self.firstname.fill(firstname)

    def register_lastname(self, lastname):
        logging.info(f"Entering last name: {lastname}")
        self.lastname.fill(lastname)

    def register_address(self, address):
        logging.info(f"Entering address: {address}")
        self.address.fill(address)

    def register_city(self, city):
        logging.info(f"Entering city: {city}")
        self.city.fill(city)

    def register_state(self, state):
        logging.info(f"Entering state: {state}")
        self.state.fill(state)

    def register_zipcode(self, zipcode):
        logging.info(f"Entering zip code: {zipcode}")
        self.zipcode.fill(zipcode)

    def register_phonenumber(self, phonenumber):
        logging.info(f"Entering phone number: {phonenumber}")
        self.phonenumber.fill(phonenumber)

    def register_ssn(self, ssn):
        logging.info("Entering SSN")
        self.ssn.fill(ssn)

    def register_username(self, username):
        logging.info(f"Entering username: {username}")
        self.username.fill(username)

    def register_password(self, password):
        logging.info("Entering password")
        self.password.fill(password)

    def register_confirmpassword(self, confirmpassword):
        logging.info("Entering confirm password")
        self.confirmpassword.fill(confirmpassword)

    def login_button(self):
        logging.info("Clicking the Register button")
        self.button.click()