# AI QDA Workshop

Publiczne materiały dla osób uczestniczących w warsztacie wykorzystania AI i
dużych modeli językowych w jakościowej analizie danych. Warsztat pokazuje cztery
sposoby organizowania i wspierania tego samego procesu kodowania: od
kontrolowanej rozmowy z modelem, przez pracę w programie CAQDAS, po
prototypowanie prostego workflow i jego lokalne uruchomienie.

Pełny układ zajęć znajduje się w
[`harmonogram_warsztatu_AI_QDA.md`](harmonogram_warsztatu_AI_QDA.md).

## Zacznij tutaj

1. Przed zajęciami sprawdź
   [`checklistę techniczną`](00_github_colab/checklista_przed_zajeciami.md).
2. Jeżeli nie znasz GitHuba lub Colaba, zacznij od
   [`00_github_colab/`](00_github_colab/).
3. Opis i materiały wspólnego korpusu znajdują się w
   [`01_data/prekariat/`](01_data/prekariat/).
4. Przed częścią Vibe Coding obejrzyj
   [referencyjną książkę kodową i graf relacji](01_data/codebook/).
5. Notebooki do ćwiczeń znajdują się bezpośrednio w
   [`04_vibe_coding/`](04_vibe_coding/), a małe wprowadzenie do pracy lokalnej
   z Codexem w [`05_ai_programming/`](05_ai_programming/).

## Cztery ścieżki pracy

| Ścieżka | Środowisko | Na czym polega praca badacza | Rola AI | Główny rezultat |
| --- | --- | --- | --- | --- |
| [1. AI Prompting for QDA](02_ai_prompting/) | ChatGPT lub Gemini | Badacz definiuje problem, jednostkę analizy, potrzebny kontekst, kolejne kroki instrukcji, format odpowiedzi i kryteria oceny. Następnie porównuje warianty promptu i sprawdza propozycje na próbce materiału. | Model odpowiada na kontrolowane instrukcje i proponuje kandydackie rezultaty, które wymagają interpretacji i oceny. | Sprawdzony prompt analityczny, procedura pracy na próbce oraz jawne kryteria oceny odpowiedzi AI. |
| [2. AI-assisted QDA Coding](03_ai_assisted_coding/) | MAXQDA z funkcjami AI oraz ChatGPT | Badacz pracuje bezpośrednio z segmentami korpusu, porównuje kodowanie człowieka i AI, rozwija system kodów, zapisuje memos oraz podejmuje decyzje o scalaniu, rozdzielaniu i doprecyzowywaniu kodów. | AI wspiera kodowanie i porządkowanie materiału, ale nie zatwierdza kodów ani interpretacji. | Zakodowany projekt MAXQDA, uporządkowany system kodów, memos i udokumentowane decyzje badacza. |
| [3. Vibe Coding for QDA](04_vibe_coding/) | Google Colab i Gemini | Badacz przekłada procedurę analityczną na dane wejściowe, oczekiwane wyniki, etapy przetwarzania, kontrole i punkty decyzyjne. Na próbce korpusu buduje małe fragmenty kodu do wyboru istotnych fragmentów, kodowania, porządkowania propozycji i tworzenia prostych statystyk. | Czat pomaga przekształcać instrukcje w uruchamialny kod. Wyniki modelu pozostają propozycjami do przeglądu. | Prototyp workflow działający na próbce, ustrukturyzowane artefakty kodowania i porównanie z wynikiem referencyjnym dla pełnego korpusu. |
| [4. AI Programming for QDA](05_ai_programming/) | GitHub, Codex i Python | Badacz poznaje strukturę projektu, uruchamia przygotowane rozwiązanie, śledzi przepływ danych, sprawdza wyniki i wykonuje jedną niewielką, kontrolowaną zmianę. | Codex pomaga czytać pliki, uruchamiać testy i implementować zmianę zgodnie z opisanym kontraktem. | Walidacja wyniku na próbce, prosty test, commit oraz zrozumienie, jak prototyp może być dalej rozwijany. |

Każda ścieżka pracuje na tym samym problemie badawczym i rozwijanej książce
kodowej, ale wykorzystuje inne środowisko i inaczej rozkłada pracę między
badacza, model oraz oprogramowanie. Kontrola techniczna nie oznacza jeszcze, że
kod lub kategoria są trafne analitycznie.

## Otwórz notebooki w Colabie

[![Notebook 00: start](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/00_github_colab/00_start_here_github_colab.ipynb)
[![Notebook 01: Gemini](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/00_github_colab/01_colab_gemini_vibe_coding.ipynb)

[![Vibe 1: jednostki tekstu](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/04_vibe_coding/01_od_transkrypcji_do_jednostek.ipynb)
[![Vibe 2: kodowanie opisowe](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/04_vibe_coding/02_od_relewantnego_fragmentu_do_kodu_D.ipynb)
[![Vibe 3: kodowanie zogniskowane](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/04_vibe_coding/03_od_kodow_D_do_wzorcow_F.ipynb)
[![Vibe 4: książka kodowa](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caqdastm/ai_qda-workshop-1u/blob/main/04_vibe_coding/04_od_wzorcow_do_ksiazki_TSFD.ipynb)

Odznaki otwierają wzorcowe notebooki z publicznego repozytorium. Własną pracę
zapisuj w swoim forku i otwieraj w Colabie przez **Plik -> Otwórz notatnik ->
GitHub**. Szczegóły zawiera
[`instrukcja pracy z forkiem i Colabem`](00_github_colab/instrukcja_konto_fork_colab.md).

## Struktura repozytorium

```text
00_github_colab/          wprowadzenie do GitHuba, Colaba i Gemini
01_data/                  wspólny korpus i referencyjna książka kodowa
02_ai_prompting/          AI Prompting for QDA
03_ai_assisted_coding/    AI-assisted QDA Coding
04_vibe_coding/           notebooki i materiały Vibe Coding
05_ai_programming/        małe wprowadzenie do GitHuba, Codexa i testów
06_outputs/               miejsce na wyniki pracy uczestników
```

Materiały do ścieżek `02` i `03` będą uzupełniane po zsynchronizowaniu części
przygotowywanej przez współautora.

## Zasady pracy

- Nie nadpisuj danych źródłowych w `01_data/`.
- Własne wyniki zapisuj w `06_outputs/` lub w swoim forku repozytorium.
- Nie umieszczaj w Git kluczy API, haseł, tokenów ani danych wrażliwych.
- Kod wygenerowany z AI uruchamiaj najpierw na małej próbce i sprawdzaj wynik.
- Zapisuj ważne decyzje, wątpliwości oraz zmiany wprowadzone w procedurze.
- Traktuj wyniki AI jako propozycje. O trafności kodu i kategorii decyduje badacz.

Repozytorium zawiera wyłącznie materiały uczestnika. Kod procedur autorskich,
logi modeli, materiały recenzenckie i pełne zaplecze analityczne nie są tutaj
publikowane.
