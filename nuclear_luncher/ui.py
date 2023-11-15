"""UI code."""
from importlib import import_module

from nuclear_luncher import Config

from dash import Dash
from flask import Flask


def register_dash_pages(app: Flask, routes_pathname_prefix: str = "/ui/") -> None:
    """Register dash pages."""
    dash_app = Dash(name="luncher", server=app, routes_pathname_prefix=routes_pathname_prefix)
    if Config.DEBUG:
        dash_app.enable_dev_tools(debug=True, dev_tools_prune_errors=False)

    current = import_module("nuclear_luncher.dash_pages.index")
    dash_app.layout = current.layout(dash_app)
