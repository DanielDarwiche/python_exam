from behave import given, when, then
from playwright.sync_api import expect

@given('har inte favoritmarkerat en bok')
def not_marking_book_as_favorite(context):
    pass

@when('användaren är på sidan "Mina böcker"')
def click_favorite_books_button(context):
    page = context.page
    favorite_books_button = page.get_by_role("button", name="Mina böcker")
    favorite_books_button.click()

@then('ska ett felmeddelande visas eftersom det inte finns en favoritbok')
def verify_no_favorite_books_error_message(context):
    page = context.page
    error_message = page.locator('p', has_text="När du valt, kommer dina favoritböcker att visas här.")
    expect(error_message).to_be_visible()
