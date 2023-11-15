# models.py
"""Database models."""

from dataclasses import dataclass

from sqlalchemy import Column, Float, ForeignKey, Integer, Text
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base sqlalchemy ORM model."""


@dataclass
class Ingredient(Base):
    """Ingredient table model."""

    __tablename__ = "ingredient"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)  # noqa: A003
    name = Column(Text, nullable=False, unique=True)
    unit = Column(Text, nullable=False)


@dataclass
class Dishes(Base):
    """Dishes table model."""

    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)  # noqa: A003
    name = Column(Text, nullable=False, unique=True)


@dataclass
class Recipe(Base):
    """Recipe table model."""

    __tablename__ = "recipe"

    dishes_id = Column(Integer, ForeignKey("dishes.id"), primary_key=True, nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredient.id"), primary_key=True, nullable=False)
    quantity = Column(Float, nullable=False)
