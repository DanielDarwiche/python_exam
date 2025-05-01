Feature: Markera bok som favorit
  Som användare vill jag kunna markera en bok som favorit i katalogen.

  Scenario: Hjärtsymbol visas när användaren hovrar över en bok
    Given att användaren ser bokkatalogen
    When användaren hovrar över en bok
    Then ska en hjärtsymbol visas på boken

  Scenario: Användaren markerar en bok som favorit och ser den under "Mina böcker"
    Given att användaren ser bokkatalogen
    And en hjärtsymbol visas på en bok
    When användaren klickar på hjärtsymbolen
    And användaren klickar på "Mina böcker"
    Then ska den markerade boken visas i listan över favoritböcker
