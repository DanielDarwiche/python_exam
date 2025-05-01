Feature: Visa favoritböcker
  Som användare vill jag kunna se alla böcker som är favoritmarkerade när jag har tryckt på knappen "Mina böcker".

  Scenario: Användaren klickar på knappen "Mina böcker" och ser favoritböcker
    Given att användaren är på startsidan
    And har favoritmarkerat en bok
    When användaren klickar på knappen "Mina böcker"
    Then ska en favoritbok visas

  Scenario: Användaren klickar på knappen "Mina böcker" och ser inga böcker
    Given att användaren är på startsidan
    When användaren klickar på knappen "Mina böcker"
    And har inte favoritmarkerat en bok
    Then ska ett felmeddelande visas eftersom det inte finns en favoritbok
