"""Index layout."""
from data.db import get_ingredients

from dash import Dash, dash_table, dcc, html


def layout(dash_app: Dash) -> html.Div:
    """Layout."""
    data = get_ingredients()
    dash_app.layout = html.Div(
        [
            html.H1("Items Table"),
            dash_table.DataTable(
                id="items-table",
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
                data=[data],
            ),
            dcc.Graph(
                id="example-graph",
                figure={
                    "data": [
                        {
                            "x": [1, 2, 3],
                            "y": [4, 1, 2],
                            "type": "bar",
                            "name": "SF",
                        },
                        {
                            "x": [1, 2, 3],
                            "y": [2, 4, 5],
                            "type": "bar",
                            "name": "Montreal",
                        },
                    ],
                    "layout": {
                        "title": "Dash Graph",
                    },
                },
            ),
        ],
    )
    return dash_app.layout
