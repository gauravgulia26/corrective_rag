import os

from dotenv import load_dotenv

load_dotenv()
from langchain_typesafe import TypeSafeClassifier


def get_system_one_model() -> TypeSafeClassifier:
    return TypeSafeClassifier(api_key=os.getenv("TYPESAFE_API_KEY"))
