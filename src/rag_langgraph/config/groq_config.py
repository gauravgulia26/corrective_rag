from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class GroqConfig:
    model_name: str
    temperature: float
    max_tokens: int
    max_retries: int
    reasoning_effort: str = None
