"""Application code."""

from os import environ
from typing import Literal


class Config:
    """Configuration variables."""

    # General Config
    """DEBUG = environ.get("FLASK_DEBUG")"""
    DEBUG = True
    LOG_GROUP = environ.get("LOG_GROUP", "none")
    STAGE: Literal["dev", "integration", "staging", "production"] = environ.get("STAGE", "dev").lower()  # type: ignore[assignment]
    XRAY_ENABLED = environ.get("STAGE", "dev").lower() != "dev"
