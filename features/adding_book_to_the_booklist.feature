@addbook
Feature: Lägga till bok i katalog
  Som användare vill jag kunna lägga till en bok i katalogen

  Scenario: Användaren kan inte lägga till en bok med Författare och utan Titel
    Given att användaren är på rätt sida
    When användaren anger Författare men inte Titel
    Then går det inte att trycka på knappen "Lägg till ny bok"

  Scenario: Användaren lägga till en bok med Titel och Författare
    Given att användaren är på rätt sida
    When användaren angivit Författare och Titel
    Then går det att trycka på knappen "Lägg till ny bok"




