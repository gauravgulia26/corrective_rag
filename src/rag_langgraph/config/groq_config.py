from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class GroqConfig:
    model_name: str
    temperature: float
    max_tokens: int | None = None
    max_retries: int | None = 3
    reasoning_effort: str = None
