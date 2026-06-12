import logging
from playwright.sync_api import expect
import config
import pytest
from utils.data_reader import load_json_data
from pages.form_page import FormPage

test_data=load_json_data("testdata/login_data.json")

@pytest.mark.parametrize("data", test_data)

def test_form(page, data):
    logging.info("Form opening...")
    form=FormPage(page)
    logging.info("Navigating...")
    form.navigate()
    logging.info("Adding data...")
    form.login_username(data["username"])
    logging.info("Adding data...")
    form.login_password(data["password"])
    logging.info("Clicking login button...")
    form.login_button()
    error = page.locator("#name")
    expect(error).to_contain_text(data["expected"])
    page.screenshot(path="login.png")
    

