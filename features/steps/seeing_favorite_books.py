from behave import given, when, then
from playwright.sync_api import expect

@given('att användaren är på startsidan')
def go_to_homepage(context):
    # Setup görs i environment.py
    pass

@given('har favoritmarkerat en bok')
def mark_book_as_favorite(context):
    page = context.page
    first_book = page.locator('div.catalog > div.book').first
    first_book.hover()
    # Vänta på att hjärtikonen syns och klicka på den
    heart_icon = first_book.locator('[data-testid^="star-"][role="button"]')
    heart_icon.wait_for(state='visible', timeout=5000)
    heart_icon.click()

@given('har inte favoritmarkerat en bok')
def not_marking_book_as_favorite(context):
    # Ingen åtgärd behövs, grundläge
    pass

@when('användaren klickar på knappen "Mina böcker"')
def click_favorite_books_button(context):
    page = context.page
    favorite_books_button = page.get_by_role("button", name="Mina böcker")
    favorite_books_button.click()

@then('ska en favoritbok visas')
def verify_favorite_book_is_visible(context):
    page = context.page
    page.wait_for_selector('ol > li')
    favorite_book = page.locator('ol > li').first
    expect(favorite_book).to_be_visible()

@then('ska ett felmeddelande visas eftersom det inte finns en favoritbok')
def verify_no_favorite_books_error_message(context):
    page = context.page
    error_message = page.locator('p', has_text="När du valt, kommer dina favoritböcker att visas här.")
    expect(error_message).to_be_visible()
