from behave import given, when, then
from playwright.sync_api import expect

@given('att användaren ser bokkatalogen')
def given_user_views_catalog(context):
    context.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")

@when('användaren hovrar över en bok')
def hover_over_book(context):
    page = context.page
    first_book = page.locator('div.catalog > div.book').first
    first_book.hover()
    context.first_book = first_book
    expect(first_book).to_be_visible()

@given('en hjärtsymbol visas på en bok')
def viewing_heart_symbol(context):
    page = context.page
    first_book = page.locator('div.catalog > div.book').first
    first_book.hover()
    context.first_book = first_book
    heart_symbol = first_book.locator('[data-testid^="star-"][role="button"]')
    expect(heart_symbol).to_be_visible()
    context.heart_symbol = heart_symbol

@then('ska en hjärtsymbol visas på boken')
def verify_heart_symbol(context):
    heart_symbol = context.first_book.locator('[data-testid^="star-"][role="button"]')
    expect(heart_symbol).to_be_visible()
    context.heart_symbol = heart_symbol

@when('användaren klickar på hjärtsymbolen')
def click_heart_symbol(context):
    context.heart_symbol.click()

@when('användaren klickar på "Mina böcker"')
def viewing_favoritebooks(context):
    page = context.page
    favorite_books_button = page.get_by_role("button", name="Mina böcker")
    favorite_books_button.click()

@then('ska den markerade boken visas i listan över favoritböcker')
def favorite_book_visible(context):
    page = context.page
    page.wait_for_selector('ol > li')
    favorite_book = page.locator('ol > li').first
    expect(favorite_book).to_be_visible()
