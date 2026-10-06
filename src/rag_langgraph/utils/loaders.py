from pathlib import Path
from typing import Any

import yaml

from rag_langgraph.settings.base import LoadBaseSettings


def load_params(path: str | Path) -> dict[str, Any]:
    """
    Load parameters from a YAML file.

    Args:
        path: Path to the YAML parameter file.

    Returns:
        Dictionary containing the loaded parameters.

    Raises:
        FileNotFoundError: If the parameter file does not exist.
        ValueError: If the path is not a file or YAML content is invalid.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Parameter file not found: {path}")

    if not path.is_file():
        raise ValueError(f"Parameter path is not a file: {path}")

    try:
        with path.open("r", encoding="utf-8") as file:
            params = yaml.safe_load(file)

    except yaml.YAMLError as exc:
        raise ValueError(f"Invalid YAML file: {path}") from exc

    if params is None:
        return {}

    if not isinstance(params, dict):
        raise TypeError(
            f"Expected YAML root to be a mapping, got {type(params).__name__}"
        )

    return params


def load_settings(
    model_config: Any,
    param_file_path: str | Path,
    nested: bool = True,
    param_key: str | None = None,
) -> LoadBaseSettings:
    if nested and not param_key:
        raise ValueError("Nested True need param key, kindly pass the param key.")

    prms = load_params(path=param_file_path)[param_key]
    return LoadBaseSettings(llm_config=model_config(**prms))


def load_prompt(path: str | Path) -> str:
    """
    Load a prompt file and return its content as clean text.

    Parameters
    ----------
    path:
        Path to the prompt file.

    Returns
    -------
    str
        Prompt content with leading/trailing whitespace removed.
    """
    prompt_path = Path(path)

    if not prompt_path.is_file():
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    return prompt_path.read_text(encoding="utf-8").strip()
