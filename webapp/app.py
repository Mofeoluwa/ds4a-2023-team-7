import dash
from dash import Dash, dcc, html, Input, Output, State, dash_table, callback
import dash_mantine_components as dmc
import plotly.express as px
from dash import Dash, dcc, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd
from datetime import *
from app_styles import *
from data.dhs_data import *

external_stylesheets = [dbc.themes.DARKLY]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

date_range_select = dcc.DatePickerRange(
        style=date_picker_style,
        id="date-range",
        min_date_allowed=datetime(2013, 1, 1),
        max_date_allowed=datetime.today(),
        start_date=datetime(2013, 1, 1),
        end_date=datetime.today(),
    )

metric_select = dhs_daily_df.columns

output = dcc.Graph(style=graph_col_style,
                   id="graph")

app.layout = dbc.Container([
    dcc.Markdown(
            "# Exploring Housing Insecurity in NYC",
            style={"textAlign": "center"},
            className="header",
        ),
    
    dbc.Row([
        dbc.Tabs(
            id='tabs',
            children=[
                dcc.Tab(
                    label='YoY Time Series',
                    children=[
                        dbc.Row(children= [date_range_select],justify='center'),
                        dbc.Row(children= [output]),
                    ]
                ) 
            ]
            
        )
    ])
])


