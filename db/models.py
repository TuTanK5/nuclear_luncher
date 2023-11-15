# models.py
"""Database models."""

from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base sqlalchemy ORM model.

    Args:
        DeclarativeBase (_type_): _description_
    """


class Ingredient(Base):
    """
    Ingredient table model.

    Args:
        Base (_type_): _description_
    """

    __tablename__ = "ingredient"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)  # noqa: A003
    name = Column(Text, nullable=False)
    unit = Column(Text, nullable=False)


class Dishes(Base):
    """
    Dishes table model.

    Args:
        Base (_type_): _description_
    """

    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)  # noqa: A003
    name = Column(Text, nullable=False)


class Recipe(Base):
    """
    Recipe table model.

    Args:
        Base (_type_): _description_
    """

    __tablename__ = "recipe"

    dishes_id = Column(Integer, ForeignKey("dishes.id"), primary_key=True, nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredient.id"), primary_key=True, nullable=False)
    quantity = Column(Float, nullable=False)
