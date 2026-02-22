import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hostnplay.com/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("demo@hostnplay.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Demo12.")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("button", name="Create Game").click()
    page.get_by_text("x", exact=True).click()
    page.get_by_text("Create New Game").click()
    page.get_by_text("Upload Your ImageClick to").click()
    page.locator("body").set_input_files("no-avatar.jpg")
    page.get_by_role("button", name="Open AI").click()
    page.locator("div").filter(has_text="Create a competitive Warzone").nth(5).click()
    page.get_by_role("button").nth(2).click()
    page.get_by_role("button", name="Next").click()
    page.get_by_role("button", name="Submit").click()
    page.get_by_text("28").click()
    page.locator("input[type=\"time\"]").click()
    page.locator("input[type=\"time\"]").fill("20:30")
    page.get_by_role("button", name="Generate").click()
    page.get_by_role("button", name="Schedule").click()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
