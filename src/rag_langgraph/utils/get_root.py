from __future__ import annotations

import os
from pathlib import Path


def get_project_root() -> Path:
    """Return the root directory of the project as a Path object.

    Resolution strategy:
    1. Check `PROJECT_ROOT` environment variable if explicitly set.
    2. Traverse upwards from this file looking for marker files (`pyproject.toml`, `.git`).
    3. Fallback based on known repository depth (3 levels up from `utils/get_root.py`).
    """
    env_root = os.getenv("PROJECT_ROOT")
    if env_root:
        candidate = Path(env_root).resolve()
        if candidate.exists():
            return candidate

    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / "pyproject.toml").is_file() or (parent / ".git").exists():
            return parent

    return current.parents[3]


get_root = get_project_root
PROJECT_ROOT: Path = get_project_root()
ROOT_DIR: Path = PROJECT_ROOT

__all__ = [
    "PROJECT_ROOT",
    "ROOT_DIR",
    "get_project_root",
    "get_root",
]


if __name__ == "__main__":
    print(get_project_root())
