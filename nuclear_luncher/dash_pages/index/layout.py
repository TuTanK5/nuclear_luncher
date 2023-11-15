"""Index layout."""
from data.db import get_ingredients

from dash import Dash, dash_table, html


def layout(dash_app: Dash) -> html.Div:
    """Layout."""
    data = get_ingredients()
    dash_app.layout = html.Div(
        [html.H1("Items Table"),
         dash_table.DataTable(id="items-table", columns=[{
             "name": "ID",
             "id": "id",
         }, {
             "name": "Name",
             "id": "name",
         }], data=data)],
    )
    return html.Div()
