import dash
from dash import Dash, dcc, html, Input, Output, State, dash_table, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from app_styles import *
from data.dhs_data import *
import assets.navigation_bar as nav
import logging

external_stylesheets = [
    dbc.themes.DARKLY,  # First stylesheet
    '/assets/style.css'  # Second stylesheet (local CSS file)
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

date_range_select = dcc.DatePickerRange(
        style=date_picker_style,
        id="date-range",
        className="standard-calendar",
        min_date_allowed=datetime(2013, 1, 1),
        max_date_allowed=datetime.today(),
        start_date=datetime(2013, 1, 1),
        end_date=datetime.today(),
    )

date_range_select_2 = dcc.DatePickerRange(
        style=date_picker_style,
        id="date-range-2",
        className="standard-calendar",
        min_date_allowed=datetime(2013, 1, 1),
        max_date_allowed=datetime.today(),
        start_date=datetime(2013, 1, 1),
        end_date=datetime.today(),
    )

metric_dropdown = dcc.Dropdown(
    id='metric-dropdown',
    className="standard-dropdown",
    options=[
        {'label': i, 'value': i} for i in dhs_daily_df.columns
    ],
    value=dhs_daily_df.columns[0],
    style=standard_drop_down,
    multi=True,
    clearable=True
)

metric_dropdown_2 = dcc.Dropdown(
    id='metric-dropdown-2',
    className="standard-dropdown",
    options=[
        {'label': i, 'value': i} for i in dhs_daily_df.columns
    ],
    value=dhs_daily_df.columns[0],
    style=standard_drop_down,
    multi=True,
    clearable=True
)

button = dbc.Button(
    "Submit",
    id='run-button',
    className='standard-button',
    style=buttons
)

button_2 = dbc.Button(
    "Submit",
    id='run-button-2',
    className='standard-button',
    style=buttons
)

output = dcc.Graph(style=graph_col_style,
                   id="graph")

output_2 = dcc.Graph(style=graph_col_style,
                   id="graph-2")

app.layout = html.Div(
    children=[
        nav.NavBarHeader('Investigating Housing Insecurity in NYC'),
        html.Div(
            id='page-header',
            children=[
                dbc.Container([
                    html.Link(
                        rel='stylesheet',
                        href=app.get_asset_url('style.css')
                    ),
                    dcc.Markdown(
                        '''
                        ###### Rah McRae
                        ''',
                        style=header_name,
                        className="header",
                    ),
                    html.Br(),
                    dbc.Row(
                        [
                            dbc.Tabs(
                                id='tabs',
                                children=[
                                    dcc.Tab(
                                        label='Time Series Analysis',
                                        children=[
                                            dbc.Row(
                                                children=[date_range_select, metric_dropdown, button],
                                                justify='center'
                                            ),
                                            dbc.Row(children=[output], justify='center'),
                                        ]
                                    ),
                                    dcc.Tab(
                                        label='Other Analysis',
                                        children=[
                                            dbc.Row(
                                                children=[date_range_select_2, metric_dropdown_2, button_2],
                                                justify='center'
                                            ),
                                            dbc.Row(children=[output_2], justify='center'),
                                        ]
                                    ),
                                ]
                            )
                        ]
                    ),
                ])
            ]
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)


