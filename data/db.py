"""Database query codes."""

from data.models import Ingredient, Recipe  # noqa: F401


def get_ingredients() -> dict[str, str]:
    """Query list of ingredients from db."""

    return {"id": "1", "name": "name", "unit": "kg"}


def get_recipes() -> list[Recipe]:
    """Query list of recipes from db."""

    return []
