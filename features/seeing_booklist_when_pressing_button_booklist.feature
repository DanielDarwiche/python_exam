@booklist
Feature: Visa katalog
  Som användare vill jag kunna se alla böcker när jag har tryckt på knappen "Katalog".

  Scenario: Användaren klickar på knappen "Katalog" och ser en lista med böcker
    Given att användaren är på sidan "Mina böcker"
    When användaren klickar på knappen "Katalog"
    Then ska en lista med böcker visas
