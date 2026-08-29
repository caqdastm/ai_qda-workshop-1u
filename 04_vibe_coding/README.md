# Cztery notebooki uczestnika

## Punkt Odniesienia

Zanim zaczniesz budować własny podstawowy pipeline, poświęć około 10 minut na
obejrzenie wyniku referencyjnego opracowanego na całym korpusie:

1. Przeczytaj jedną pełną gałąź `T -> S -> F -> D` w
   [finalnej książce kodowej](../01_data/codebook/codebook_prekariat_final.md).
2. Porównaj 2-3 [karty kodów S](../01_data/codebook/synthetic_codes.csv),
   zwracając uwagę na definicję oraz kryteria włączenia i wyłączenia.
3. Otwórz [graf relacji](../01_data/codebook/relational-codebook-graph.html) w
   widoku `F-F + T-T` i odczytaj jedną ścieżkę przyczynową lub strategiczną z
   pomocą [legendy](../01_data/codebook/relation_legend.md).

Nie analizuj teraz całej książki. Ten krótki ogląd pokazuje, do jakiego rodzaju
artefaktu prowadzą kolejne ćwiczenia; nie jest kluczem odpowiedzi dla próbki.

## Kolejność Pracy

Każdy notebook jest małym etapem pipeline'u kodowania AI_QDA. Otwieraj je po
kolei; artefakty są przekazywane przez `MyDrive/AI_QDA_Workshop`.

1. [Od transkrypcji do jednostek](01_od_transkrypcji_do_jednostek.ipynb) —
   projektowanie kontraktu jednostki i śladu do źródła.
2. [Od relewantnego fragmentu do D](02_od_relewantnego_fragmentu_do_kodu_D.ipynb) —
   rozdzielenie relewancji od przypisania 0-n kodów D.
3. [Od D do F](03_od_kodow_D_do_wzorcow_F.ipynb) — porównanie profili D,
   wspólny mechanizm, granica i przypadek negatywny.
4. [Od F do książki T–S–F–D](04_od_wzorcow_do_ksiazki_TSFD.ipynb) — jedna
   operacyjna karta S, oszczędny T, walidacja i handoff do Codexa.

## Wspólna pętla

```text
model kodowania i cel etapu
  -> potrzebna procedura
  -> karta procedury badawczej
  -> zwinięty dodatek techniczny
  -> instrukcja i mała funkcja napisana w czacie Colaba
  -> checklista i inspekcja fragmentów
  -> dwa porównywane prompty analityczne przez API
  -> decyzja badacza
  -> artefakt dla następnego bloku
```

Kod nie jest tworzony przez API. Uczestnik przekazuje instrukcję do czatu AI
w Colabie i wkleja jedną otrzymaną funkcję. Każdy notebook używa maksymalnie
dwóch wywołań API wyłącznie do porównania wyników analitycznych.

Wspólny adapter pozwala wybrać `gemini` albo `openai` bez zmiany dalszych
komórek. Klucze pozostają w Colab Secrets, a przy OpenAI uczestnik osobno
wybiera wartość `store`. Log lokalny zapisuje provider, model, prompt,
odpowiedź, wartość `store` i dostępny identyfikator odpowiedzi. Domyślny `mock`
nie wysyła danych i nie wytwarza propozycji analitycznych.

Przygotowany `workshop_support.py` obsługuje tylko ograniczony pakiet materiału,
API, log i pliki. Nie zawiera dostrojonych promptów ani logiki budującej kody
D/F/S/T. Pełny wynik referencyjny pokazuje możliwy rezultat skali; nie jest
kluczem odpowiedzi dla ćwiczeń.
