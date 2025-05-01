## För att köra testerna

- För att köra alla tester behöver man skriva i terminalen:

      behave

---
## Feature: Se favoritböcker

- När användaren **inte har någon favoritbok** ska ingen favoritbok visas, samt ett meddelande för detta.
- När användaren **har en favoritbok** ska favoritboken visas.

För att köra alla tester för **seeing_favoritebooks_when_pressing_button_favoritebooks** så kan man nyttja taggen för nämnda feature och skriva i terminalen:

    behave --tags=favoritbok
---
## Feature: Se katalogen

- Användaren ska kunna se hela katalogen av böcker.

För att köra alla tester för **seeing_booklist_when_pressing_button_booklist** så kan man nyttja taggen för nämnda feature och skriva i terminalen:

    behave --tags=booklist
---
## Feature: Lägga till book i katalogen

- Användaren ska kunna lägga till en bok i katalogen, om Titel och Författare är angivet.
- Användaren ska inte kunna lägga till en bok i katalogen, om Författare är angivet men Titel inte är angivet.

För att köra alla tester för **adding_book_to_the_booklist** så kan man nyttja taggen för nämnda feature och skriva i terminalen:

    behave --tags=addbook
---
## Feature: Markera bok som favorit

- Användaren ska kunna se ett hjärta när användaren hovrar musen över en bok i katalogen.
- Användaren ska kunna trycka på hjärtat på en bok så att den markeras som favorit.
- Användaren ska kunna se om sina favoritböcker på sidan "Mina böcker".

För att köra alla tester för **adding_book_as_a_favorite** så kan man nyttja taggen för nämnda feature och skriva i terminalen:

    behave --tags=addfavo