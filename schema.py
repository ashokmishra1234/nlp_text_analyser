"""
schema.py
=========
All Pydantic models for request validation and response structure.
FastAPI uses these to auto-validate incoming JSON and generate Swagger docs.
"""

from pydantic import BaseModel


# ─── REQUEST SCHEMA ───────────────────────────────────────────────────────────

class TextInput(BaseModel):
    """Input schema — used by all 3 endpoints."""
    text: str

    class Config:
        json_schema_extra = {
            "example": {
                "text": "FastAPI is an amazing framework for building APIs quickly."
            }
        }


# ─── RESPONSE SCHEMAS ─────────────────────────────────────────────────────────

class SentimentResponse(BaseModel):
    """Response schema for /sentiment endpoint."""
    text: str
    sentiment: str      # Positive / Negative / Neutral
    polarity: float     # -1.0 to +1.0
    subjectivity: float # 0.0 to 1.0


class KeywordResponse(BaseModel):
    """Response schema for /keywords endpoint."""
    text: str
    keywords: list[str]


class SummaryResponse(BaseModel):
    """Response schema for /summarize endpoint."""
    original_text: str
    summary: str
    original_word_count: int
    summary_word_count: int
