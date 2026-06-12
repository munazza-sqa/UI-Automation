import logging
import config
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page(): 
    logging.basicConfig(filename="automation.log", level=logging.INFO, format="%(asctime)s-%(levelname)s-%(message)s", force=True)
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=config.HEADLESS, slow_mo=config.SLOW_MO)
        context=browser.new_context(record_video_dir=config.VIDEO_DIR)
        page=context.new_page()
        #page.set_default_timeout(config.TIME_OUT)
        yield page
        context.close()
        browser.close()
