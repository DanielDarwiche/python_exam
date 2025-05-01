from behave import given, when, then
from playwright.sync_api import expect

@given('att användaren är på sidan "Mina böcker"')
def on_my_books_page(context):
    page = context.page
    my_books_button = page.get_by_role("button", name="Mina böcker")
    my_books_button.click()

@when('användaren klickar på knappen "Katalog"')
def when_click_catalog_button(context):
    page = context.page
    catalog_button = page.get_by_role("button", name="Katalog")
    catalog_button.click()

@then('ska en lista med böcker visas')
def then_booklist_is_visible(context):
    page = context.page
    page.wait_for_selector('div.catalog > div.book')
    books = page.locator('div.catalog > div.book')
    expect(books.first).to_be_visible()
