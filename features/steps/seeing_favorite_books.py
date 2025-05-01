from behave import given, when, then
from playwright.sync_api import expect

@given('att användaren är på startsidan')
def go_to_homepage(context):
    # Setup görs i environment.py
    pass

@given('har favoritmarkerat en bok')
def mark_book_as_favorite(context):
    page = context.page
    first_book = page.locator('ol > li').first
    first_book.hover()
    heart_icon = first_book.locator('[data-testid^="star-"][role="button"]')
    heart_icon.click()

@when('användaren klickar på knappen "Mina böcker"')
def click_favorite_books_button(context):
    page = context.page
    favorite_books_button = page.get_by_role("button", name="Mina böcker")
    favorite_books_button.click()

@then('ska en favoritbok visas')
def verify_favorite_book_is_visible(context):
    page = context.page
    favorite_book = page.locator('ol > li').first
    expect(favorite_book).to_be_visible()
