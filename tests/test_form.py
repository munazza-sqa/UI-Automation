import logging
import random
import time
import allure
import pytest
from playwright.sync_api import expect
from pages.form_page import FormPage
from utils.data_reader import load_json_data

test_data = load_json_data("testdata/login_data.json")

@pytest.mark.parametrize("data", test_data)
def test_form(page, data):  
    logging.info(f"STARTING TEST: Registration validation for user")
        
    delay = random.uniform(2.5, 4.5)
    logging.info(f"Applying pre-navigation delay: {delay:.2f}s")
    time.sleep(delay)
    
    logging.info("Initializing FormPage POM and navigating to registration route.")
    form = FormPage(page)
    form.navigate()
    
    # 2. Fill out form fields
    logging.info(f"Beginning data entry workflow for registration form.")
    form.register_firstname(data["firstname"])
    form.register_lastname(data["lastname"])
    form.register_address(data["address"])
    form.register_city(data["city"])
    form.register_state(data["state"])
    form.register_zipcode(data["zipcode"])
    form.register_phonenumber(data["phonenumber"])
    form.register_ssn(data["ssn"])
    form.register_username(data["username"])
    form.register_password(data["password"])
    form.register_confirmpassword(data["confirmpassword"])
    
    submit_delay = random.uniform(0.5, 1.2)
    logging.info(f"Form entry completed. Pausing for {submit_delay:.2f}s before clicking submit.")
    time.sleep(submit_delay)
    
    logging.info("Submitting registration form via login_button.")
    form.login_button()
    
    logging.info("Waiting for Cloudflare verification screen to detach...")
    page.get_by_text("Performing security verification").wait_for(state="detached", timeout=15000)
    logging.info("Application response page received.")
    
    try:
        logging.info(f"Executing text assertion block searching for target: '{data['expected']}'")
        expect(page.locator("body")).to_contain_text(data["expected"], timeout=12000)
        logging.info(f"SUCCESS: Validation text match confirmed for user '{data['username']}'.")
    except AssertionError as error:
        logging.error(f"FAILURE: Assertion mismatch for user '{data['username']}'.")
        raise error
    finally:
        logging.info("Generating execution snapshot for Allure reporting.")
        screenshot_bytes = page.screenshot()
        allure.attach(
            screenshot_bytes, 
            name="Execution_Screenshot", 
            attachment_type=allure.attachment_type.PNG
        )
        logging.info(f"COMPLETED TEST Run for user '{data['username']}'\n")