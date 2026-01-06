import os
from playwright.sync_api import sync_playwright

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")

def test_homepage_opens():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL + "/", wait_until="domcontentloaded")
        assert page.content() is not None
        browser.close()

def test_login_page_opens():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL + "/login", wait_until="domcontentloaded")
        assert "login" in page.url.lower()
        browser.close()

def test_register_page_opens():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(BASE_URL + "/register", wait_until="domcontentloaded")
        assert "register" in page.url.lower()
        browser.close()
