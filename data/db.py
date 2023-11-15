"""Database query codes."""

import sqlite3

from data.models import Recipe

QUERY_GET_ALL_INGREDIENTS = """SELECT * from ingredient"""

connection = sqlite3.connect("luncher.db")


def dict_factory(cursor: sqlite3.Cursor, row: sqlite3.Row) -> dict:
    """Cast sqlite3 query result to dict."""
    fields = [column[0] for column in cursor.description]
    return dict(zip(fields, row, strict=False))


connection.row_factory = dict_factory
cursor = connection.cursor()


def get_ingredients() -> list:
    """Query list of ingredients from db."""
    data = cursor.execute(QUERY_GET_ALL_INGREDIENTS).fetchall()
    connection.commit()
    connection.close()
    return data


def get_recipes() -> list[Recipe]:
    """Query list of recipes from db."""

    return []
