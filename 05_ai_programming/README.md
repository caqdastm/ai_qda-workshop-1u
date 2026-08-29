# Ścieżka 4: AI Programming For QDA

**Środowisko:** lokalne repozytorium, Codex i Python.

Ta część nie buduje drugiego pipeline'u. Uczestnik bierze cztery karty
procedur i kandydackie artefakty z Vibe Codingu, odtwarza ich zależności,
sprawdza kontrakty oraz wykonuje jedną małą, testowalną zmianę z Codexem.

## Przygotuj Handoff

1. Pobierz z Dysku Google `AI_QDA_Workshop_handoff.zip`, utworzony przez
   ostatni notebook modułu 04.
2. Rozpakuj go w lokalnym klonie do
   `06_outputs/uczestnicy/AI_QDA_Workshop/`. Ten katalog jest ignorowany przez
   Git.
3. Wypełnij [brief jednej adaptacji](codex_adaptation_brief.md).
4. Przejdź przez [pełny scenariusz czterech godzin](przejscie_z_vibe_coding.md).

To nadal warsztat o kodowaniu AI_QDA: adaptujemy sposób wyboru jednostek,
kodowania D, budowy F/S/T i kontroli śladu w danych. Nie przenosimy do niego
celów ani produktów analizy tematycznej. Wspólna z drugim warsztatem jest
struktura uczenia: badacz opisuje model i cel, model proponuje kod, test
sprawdza zachowanie techniczne, a badacz ocenia sens analityczny.

## Cel 4 Godzin

Po bloku uczestnik potrafi:

- wskazać zależności między plikami procesu;
- zwalidować hierarchię `T -> S -> F -> D` i ślad cytatów;
- odróżnić wynik sample od referencyjnego full;
- rozpoznać potrzebną procedurę przed nazwaniem zmiany technicznej;
- wykonać, sprawdzić i zapisać małą zmianę w Git;
- rozpisać punkty przyszłego workflow agentowego bez budowania pełnego agenta.

## Przebieg

1. **Inwentaryzacja:** odtwórz z kart i artefaktów przepływ jednostki → D → F → S/T.
2. **Walidacja:** sprawdź ID, rodziców, wymagane pola S, puste definicje D i
   możliwość powrotu od cytatu do tekstu.
3. **Mikrofunkcja:** nazwij problem pipeline'u, opisz potrzebną procedurę,
   poproś Codexa o implementację gotowego punktu rozszerzenia i odblokuj test.
4. **Transfer:** wypełnij brief adaptacji, nazwij role, punkty kontroli badacza
   i zapisz commit.

Gdy grupa utknie przy walidatorze, może zacząć od działającego
[fallbacku](starter/README.md) i poprosić Codexa o jedną małą rozbudowę.

**Rezultat:** nie „gotowy system agentowy”, lecz repozytorium, w którym
uczestnik rozumie przepływ danych, potrafi przełożyć cel metodologiczny na
małą funkcjonalność i ma pierwszą zweryfikowaną zmianę lokalną.
