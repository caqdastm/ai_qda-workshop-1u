"""Minimal infrastructure for the participant-facing AI_QDA notebooks.

The module handles a bounded evidence packet, provider calls, logs and files.
It deliberately contains no tuned prompts and no D/F/S/T construction logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
from typing import Any

import pandas as pd


PACKET_ROWS = [
    {
        "text_unit_id": "PREWORK_01_U0107",
        "case_id": "PREWORK_01",
        "source_file": "PREWORK_01_trans.docx",
        "sequence": 107,
        "speaker": "J",
        "text": (
            "A nawet samo to, że ona potrafi obrazić pracownika w obecności ludzi. "
            "Czyli na przykład, jak ja sprzedawałam wędliny, potrafiła do mnie "
            "podejść, naubliżać mi i wyjść. I tak, jakby jej to sprawiało radość, "
            "że ona ma tę władzę nad ludźmi."
        ),
    },
    {
        "text_unit_id": "PREWORK_01_U0119",
        "case_id": "PREWORK_01",
        "source_file": "PREWORK_01_trans.docx",
        "sequence": 119,
        "speaker": "J",
        "text": (
            "Zamykałam drzwi, żebym go nie słyszała. Albo kiedyś, jak tak mnie "
            "bardzo zdenerwowała, po prostu wyszłam przez tylne drzwi. Wiedziałam, "
            "że wrócę, bo nie wzięłam ani torebki, ani kurtki. Obeszłam sobie T. "
            "w fartuszku i wróciłam zapytać, czy szefowa już ochłonęła."
        ),
    },
    {
        "text_unit_id": "PREWORK_02_U0088",
        "case_id": "PREWORK_02",
        "source_file": "PREWORK_02_trans.docx",
        "sequence": 88,
        "speaker": "A",
        "text": (
            "Myślę, że znajomości odgrywają rolę, bo dostałam obie prace przez "
            "polecenie. To jest dość zamknięta strefa. Staram się nie palić za "
            "sobą mostów, bo kolejna szkoła najpierw dzwoni do dyrektora tej, "
            "w której pracowałam."
        ),
    },
    {
        "text_unit_id": "PREWORK_02_U0123",
        "case_id": "PREWORK_02",
        "source_file": "PREWORK_02_trans.docx",
        "sequence": 123,
        "speaker": "A",
        "text": (
            "Warunki to słabe. To, co robię i odpowiedzialność za dzieci powinny "
            "się przekładać na pensję, a zarabiamy po prostu tysiąc siedemset "
            "złotych niecałe."
        ),
    },
    {
        "text_unit_id": "PREWORK_03_U0023",
        "case_id": "PREWORK_03",
        "source_file": "PREWORK_03_trans.docx",
        "sequence": 23,
        "speaker": "A",
        "text": (
            "Nie mogę się zdecydować, czy wolałabym jeździć do pracy na osiem "
            "godzin i zapominać, czy pracować w domu. Dochodzą myśli o przyszłym "
            "macierzyństwie, a umowa o pracę mogłaby zapewnić pewien byt."
        ),
    },
    {
        "text_unit_id": "PREWORK_03_U0136",
        "case_id": "PREWORK_03",
        "source_file": "PREWORK_03_trans.docx",
        "sequence": 136,
        "speaker": "A",
        "text": (
            "Umowy zlecenia utrudniają mi dostanie kredytu. Gdyby nie to, że mąż "
            "ma umowę o pracę i przyzwoite wynagrodzenie, kredytu byśmy nie "
            "dostali. Sama szukałabym jakiejkolwiek pracy na umowę o pracę."
        ),
    },
]


def load_workshop_packet() -> pd.DataFrame:
    """Return a fresh copy of the bounded, real PREWORK evidence packet."""
    return pd.DataFrame(PACKET_ROWS).copy(deep=True)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def save_json(path: str | Path, payload: Any) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return destination


def save_dataframe(path: str | Path, frame: pd.DataFrame) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(destination, index=False)
    return destination


def load_dataframe(path: str | Path, required: list[str] | None = None) -> pd.DataFrame:
    source = Path(path)
    if not source.is_file():
        raise FileNotFoundError(f"Brak artefaktu z poprzedniego bloku: {source}")
    frame = pd.read_csv(source).fillna("")
    missing = sorted(set(required or []) - set(frame.columns))
    if missing:
        raise ValueError(f"Brak wymaganych kolumn w {source.name}: {missing}")
    return frame


def procedure_prompt(card: dict[str, str], technical_appendix: str) -> str:
    research_part = "\n".join(
        [
            "CZĘŚĆ BADAWCZA — intencja i granice procedury",
            f"Cel etapu: {card['goal']}",
            f"Wejście: {card['input']}",
            f"Widoczny rezultat: {card['observable_result']}",
            f"Kontrola techniczna: {card['automatic_check']}",
            f"Decyzja badacza: {card['researcher_decision']}",
        ]
    )
    return research_part + "\n\nDODATEK TECHNICZNY — infrastruktura notebooka\n" + technical_appendix


@dataclass
class AnalysisAPI:
    """Provider-neutral API used only for analytic calls on the corpus."""

    provider: str = "mock"
    gemini_model: str = "gemini-3.6-flash"
    openai_model: str = "gpt-5.4-mini"
    openai_store: bool = True
    authorize_api_calls: bool = False
    max_api_calls: int = 2
    runs: list[dict[str, Any]] = field(default_factory=list)
    api_call_count: int = 0

    def __post_init__(self) -> None:
        self.provider = self.provider.strip().lower()
        if self.provider not in {"mock", "gemini", "openai"}:
            raise ValueError("Wybierz provider='mock', 'gemini' albo 'openai'.")

    @property
    def model(self) -> str:
        return {
            "mock": "mock",
            "gemini": self.gemini_model,
            "openai": self.openai_model,
        }[self.provider]

    def _secret(self, name: str) -> str:
        key = os.getenv(name, "").strip()
        if key:
            return key
        try:
            from google.colab import userdata

            return str(userdata.get(name) or "").strip()
        except Exception:
            return ""

    def _mock_response(self, task_kind: str, task_label: str) -> str:
        return (
            f"MOCK — {task_kind}/{task_label}. Przepływ działa, ale ten tekst nie "
            "jest propozycją kodowania. Włącz API, aby porównywać odpowiedzi "
            "modelu, albo przejdź dalej na podstawie własnej lektury materiału."
        )

    def _call_gemini(self, prompt: str) -> tuple[str, str]:
        key = self._secret("GEMINI_API_KEY")
        if not key:
            raise RuntimeError("Dodaj GEMINI_API_KEY do Colab Secrets.")
        from google import genai

        response = genai.Client(api_key=key).models.generate_content(
            model=self.gemini_model,
            contents=prompt,
        )
        text = str(getattr(response, "text", "") or "").strip()
        response_id = str(
            getattr(response, "response_id", "") or getattr(response, "id", "") or ""
        )
        return text, response_id

    def _call_openai(self, prompt: str) -> tuple[str, str]:
        key = self._secret("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("Dodaj OPENAI_API_KEY do Colab Secrets.")
        from openai import OpenAI

        response = OpenAI(api_key=key).responses.create(
            model=self.openai_model,
            input=prompt,
            store=self.openai_store,
        )
        return str(response.output_text or "").strip(), str(response.id or "")

    def run_analysis(self, prompt: str, *, task_label: str) -> str:
        provider_response_id = ""
        if self.provider == "mock":
            response_text = self._mock_response("analytic_comparison", task_label)
        else:
            if not self.authorize_api_calls:
                raise PermissionError(
                    "Wywołania API są wyłączone. Ustaw zgodę dopiero po decyzji o danych i koszcie."
                )
            if self.api_call_count >= self.max_api_calls:
                raise RuntimeError("Osiągnięto limit wywołań API dla notebooka.")
            if self.provider == "gemini":
                response_text, provider_response_id = self._call_gemini(prompt)
            else:
                response_text, provider_response_id = self._call_openai(prompt)
            self.api_call_count += 1

        self.runs.append(
            {
                "created_at": datetime.now(timezone.utc).isoformat(),
                "task_kind": "analytic_comparison",
                "task_label": task_label,
                "provider": self.provider,
                "model": self.model,
                "prompt": prompt,
                "prompt_hash": sha256_text(prompt),
                "response": response_text,
                "provider_response_id": provider_response_id,
                "store_requested": self.openai_store if self.provider == "openai" else None,
            }
        )
        return response_text

    def export_runs(self, path: str | Path) -> Path:
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("w", encoding="utf-8") as stream:
            for row in self.runs:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
        return destination
