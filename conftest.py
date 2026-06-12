import os  # Added this to read the GitHub environment
import logging
import config
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page(): 
    logging.basicConfig(filename="automation.log", level=logging.INFO, format="%(asctime)s-%(levelname)s-%(message)s", force=True)
    
    # Check if running in GitHub Actions (CI). 
    # If yes, force headless=True and slow_mo=0. Otherwise, use your config file settings.
    is_headless = True if os.environ.get("CI") == "true" else config.HEADLESS
    slow_down = 0 if os.environ.get("CI") == "true" else config.SLOW_MO

    with sync_playwright() as p:
        # Updated this line to use the smart variables
        browser = p.chromium.launch(headless=is_headless, slow_mo=slow_down)
        
        context = browser.new_context(record_video_dir=config.VIDEO_DIR)
        page = context.new_page()
        # page.set_default_timeout(config.TIME_OUT)
        
        yield page
        context.close()
        browser.close()
        