import os
import logging
import pytest
import allure
from dotenv import load_dotenv
from playwright_stealth import Stealth 
from playwright.sync_api import sync_playwright, Error as PlaywrightError

load_dotenv()

@pytest.fixture
def page(): 
    log_file = os.getenv("LOG_FILE", "automation.log")
    
    logging.basicConfig(
        filename=log_file, 
        level=logging.INFO, 
        format="%(asctime)s-%(levelname)s-%(message)s", 
        force=True
    )
    
    # Handle Headless Logic
    if os.getenv("CI") == "true":
        is_headless = True
    else:
        is_headless = os.getenv("HEADLESS", "False").lower() == "true"
        
    # Handle Slow Mo Logic
    if os.getenv("CI") == "true":
        slow_down = 0
    else:
        slow_down = int(os.getenv("SLOW_MO", 1000))

    # Read Video Directory from .env
    video_directory = os.getenv("VIDEO_DIR", "video/")

    # Log environment setup details
    logging.info(f"Initializing test browser (Headless: {is_headless}, Slow-Mo: {slow_down}ms)")

    logging.info("Starting Playwright and launching Chromium browser")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=is_headless, slow_mo=slow_down)
    
    logging.info(f"Creating browser context (Saving videos to: {video_directory})")
    context = browser.new_context(record_video_dir=video_directory)
    
    logging.info("Applying anti-bot stealth patches to context")
    Stealth().apply_stealth_sync(context)
    
    logging.info("Opening clean browser page instance")
    page = context.new_page() 
    
    yield page
    
    # --- TEARDOWN ---
    logging.info("Tearing down environment: Closing page and browser context")
    context.close()
    browser.close()
    
    logging.info("Stopping Playwright core process")
    playwright.stop()