from behave import given, when, then
from playwright.sync_api import expect

@given('att användaren är på rätt sida')
def step_given_correct_page(context):
    page = context.page
    add_page = page.get_by_role("button", name="Lägg till bok")
    add_page.click()
    page.wait_for_timeout(3000)

@when('användaren anger Författare men inte Titel')
def step_when_author_only(context):
    page = context.page
    inputs = page.locator('div.form input')
    title_input = inputs.nth(0)
    author_input = inputs.nth(1)
    title_input.fill("")
    author_input.fill("Astrid Lindgren")
    expect(title_input).to_have_value("")
    expect(author_input).to_have_value("Astrid Lindgren")

@then('går det inte att trycka på knappen "Lägg till ny bok"')
def step_then_button_disabled(context):
    page = context.page
    add_button = page.locator('div.form button[type="submit"]')
    expect(add_button).to_be_disabled()

@when('användaren angivit Författare och Titel')
def step_when_author_and_title(context):
    page = context.page
    inputs = page.locator('div.form input')
    title_input = inputs.nth(0)
    author_input = inputs.nth(1)
    title_input.fill("Pippi Långstrump")
    author_input.fill("Astrid Lindgren")
    expect(title_input).to_have_value("Pippi Långstrump")
    expect(author_input).to_have_value("Astrid Lindgren")

@then('går det att trycka på knappen "Lägg till ny bok"')
def step_then_button_enabled(context):
    page = context.page
    add_button = page.locator('div.form button[type="submit"]')
    expect(add_button).to_be_enabled()
#
# @and('ska boken med rätt Titel och Författare synas i katalogen')
# def step_then_book_in_list(context):
#     page = context.page
#     # Anpassa selektorn nedan till hur din boklista renderas
#     book_entry = page.locator('text=Pippi Långstrump').first
#     expect(book_entry).to_be_visible()