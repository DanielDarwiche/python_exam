● vad du har testat,
● hur man startar projektet.

## För att köra alla tester behöver man skriva i terminalen:

    behave
---
## Feature: Se favoritböcker

- När användaren **inte har någon favoritbok** ska ingen favoritbok visas, samt ett meddelande för detta.
- När användaren **har en favoritbok** ska favoritboken visas.

För att köra alla tester för feature **seeing_favoritebooks_when_pressing_button_favoritebooks** så kan man nyttja taggen för nämnda feature och skriva i terminalen:

    behave --tags=favoritbok
---
