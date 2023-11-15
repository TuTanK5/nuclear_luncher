"""Index layout."""
from data.db import get_ingredients

from dash import Dash, dash_table, html


def layout(dash_app: Dash) -> html.Div:
    """Layout."""
    data = get_ingredients()
    dash_app.layout = html.Div(
        [
            html.H1("Ingredients"),
            dash_table.DataTable(
                id="ingredient-table",
                columns=[{
                    "name": "ID",
                    "id": "id",
                }, {
                    "name": "Name",
                    "id": "name",
                }, {
                    "name": "Unit",
                    "id": "unit",
                }],
                data=data,
            ),
        ],
    )
    return dash_app.layout
