# Konto, Fork I Colab

## Przed Warsztatem

1. Utwórz konto na GitHubie albo zaloguj się na istniejące konto.
2. Potwierdź adres e-mail użyty podczas rejestracji.
3. Zaloguj się na konto Google i otwórz Google Colab.
4. Nie zapisuj kluczy API ani danych logowania w notebooku.

## Utwórz Własną Kopię Materiałów

1. Otwórz repozytorium `caqdastm/ai_qda-workshop-1u`.
2. Wybierz **Fork**.
3. Jako właściciela wybierz swoje konto.
4. Utwórz fork i poczekaj, aż otworzy się jego strona.
5. Sprawdź właściciela nad listą plików. Powinna być tam Twoja nazwa, a nie
   `caqdastm`.

Repozytorium `caqdastm` jest wersją prowadzących. Podczas warsztatu pracujesz
we własnym forku. Fork nie aktualizuje się automatycznie, gdy prowadzący zmieni
materiały.

## Otwórz Notebook W Colabie

Odznaka **Otwórz w Colabie** jest adresem absolutnym i otwiera wzorzec z
repozytorium prowadzących. Fork nie przepisuje jej automatycznie. Zwykłe linki
względne między plikami na GitHubie pozostają natomiast w Twoim forku.

1. Przy pierwszym przejściu możesz użyć odznaki przy notebooku. W Colabie
   wybierz potem **Plik → Zapisz kopię w GitHubie** i jako repozytorium wskaż
   swój fork.
2. Jeśli wracasz do zapisanej pracy lub chcesz od początku użyć wersji z
   forka, wybierz w Colabie **Plik → Otwórz notatnik → GitHub**, wskaż swój
   fork i właściwy plik `.ipynb`.
3. Sprawdź nazwę właściciela repozytorium widoczną w źródle notebooka.
4. Uruchamiaj komórki od góry przyciskiem po lewej stronie komórki i zwracaj
   uwagę, czy komórka się zakończyła oraz co wyświetliła.

Notebook, runtime i pliki sesji to trzy różne warstwy:

- **notebook** przechowuje komórki i może zostać zapisany na GitHubie;
- **runtime** przechowuje bieżące wartości zmiennych i może zostać zresetowany;
- **pliki sesji** powstają w tymczasowym środowisku i znikną po jego
  zakończeniu, jeżeli ich nie pobierzesz.

## Użyj Gemini W Notebooku

W aktualnym Colabie panel AI można otworzyć ikoną Gemini w dolnej części
interfejsu. Dostęp może zależeć od konta i regionu. W tym kursie prosisz Gemini
o krótkie funkcje, a przed użyciem sprawdzasz kod i testy. Nie zezwalaj na
autonomiczne zmiany całego notebooka, kiedy ćwiczenie dotyczy jednej komórki.

Jeżeli panelu nie ma, skorzystaj z rozwiązania bazowego w notebooku albo ze
zwykłego czatu Gemini. Do wykonania modułu nie jest potrzebny klucz API.

## Zapisz Notebook Do Swojego Forka

1. Po poprawnym uruchomieniu wszystkich komórek wybierz w Colabie
   **Plik → Zapisz kopię w GitHubie**.
2. Wskaż swoje konto i własny fork.
3. Zachowaj ścieżkę w `00_github_colab/`.
4. Dla pierwszego notebooka użyj opisu `Uruchom notebook startowy Colab`.
5. Dla ćwiczenia z Gemini użyj `Dodaj pierwsze ćwiczenie vibe coding`.
6. Na stronie GitHuba sprawdź plik, diff i historię commitów.

Nie dodawaj wygenerowanych CSV do Git. W repozytorium zachowujemy notebook,
czyli procedurę, prompt, testy i decyzje. Wyniki służą w tym ćwiczeniu do
lokalnej kontroli.
