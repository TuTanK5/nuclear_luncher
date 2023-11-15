"""Flask app entry point."""
from nuclear_luncher.ui import register_dash_pages

from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def nuclear_luncher() -> Response:
    """Entry point."""
    return "<p>Hello, World!</p>"

register_dash_pages(app=app)
