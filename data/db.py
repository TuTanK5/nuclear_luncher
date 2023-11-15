"""Database query codes."""

from data.models import Ingredient, Recipe


def get_ingredients() -> list[Ingredient]:
    """Query list of ingredients from db."""

    return [Ingredient(id=1, name="ig1", unit="kg")]


def get_recipes() -> list[Recipe]:
    """Query list of recipes from db."""

    return []
