from behave import given, when, then
from playwright.sync_api import expect

@given('att användaren ser bokkatalogen')
def given_user_sees_catalog(context):
    context.page.goto("https://tap-ht24-testverktyg.github.io/exam-template/")

@when('användaren hovrar över en bok')
def when_hover_over_book(context):
    page = context.page
    first_book = page.locator('div.catalog > div.book').first
    first_book.hover()
    context.first_book = first_book
    expect(first_book).to_be_visible()

@given('en hjärtsymbol visas på en bok')
def given_heart_icon_visible(context):
    page = context.page
    first_book = page.locator('div.catalog > div.book').first
    first_book.hover()
    context.first_book = first_book
    heart_icon = first_book.locator('[data-testid^="star-"][role="button"]')
    expect(heart_icon).to_be_visible()
    context.heart_icon = heart_icon

@then('ska en hjärtsymbol visas på boken')
def then_heart_icon_visible(context):
    heart_icon = context.first_book.locator('[data-testid^="star-"][role="button"]')
    expect(heart_icon).to_be_visible()
    context.heart_icon = heart_icon

@when('användaren klickar på hjärtsymbolen')
def click_heart_icon(context):
    context.heart_icon.click()

@when('användaren klickar på "Mina böcker"')
def click_mina_bocker(context):
    page = context.page
    favorite_books_button = page.get_by_role("button", name="Mina böcker")
    favorite_books_button.click()

@then('ska den markerade boken visas i listan över favoritböcker')
def favorite_book_visible(context):
    page = context.page
    page.wait_for_selector('ol > li')
    favorite_book = page.locator('ol > li').first
    expect(favorite_book).to_be_visible()
