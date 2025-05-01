from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")
    context.playwright = playwright
    context.browser = browser
    context.page = page

def after_scenario(context, scenario):
    context.browser.close()
    context.playwright.stop()
