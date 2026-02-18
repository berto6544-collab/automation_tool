import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hostnplay.com/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("berto6544@gmail.com")
    page.get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Password").fill("Gangsta12.")
    page.wait_for_load_state('networkidle')
    page.get_by_role("button", name="Sign in").click()

    time.sleep(5)


    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)