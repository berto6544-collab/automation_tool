import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hostnplay.com/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("email@example.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("password.")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Create Game").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
