# Vasnapló

Személyes edzésnapló és coach (PWA) Soma 4 napos PPL + D programjához.

- App: https://realement.github.io/coach/
- Telefonon: nyisd meg a linket, majd „Hozzáadás a kezdőképernyőhöz”. Offline is működik.
- Adatok: a böngészőben tárolódnak; több eszközhöz a Beállítás → Szinkron résznél egy GitHub token (csak `gist` jogosultság) kell, ekkor egy titkos gistbe mentődnek.

## Fejlesztés

A forrás a `src/app-body.html`. Módosítás után: `python3 src/build.py` (előállítja a gyökérben az `index.html`, `manifest.webmanifest`, `sw.js` és ikon fájlokat).
