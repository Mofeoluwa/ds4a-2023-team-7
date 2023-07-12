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

external_stylesheets = [
                      dbc.themes.PULSE
                    , "https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap"
                    ]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)


date_range_select = dcc.DatePickerRange(
        id="date-range",
        min_date_allowed=datetime(2013, 1, 1),
        max_date_allowed=datetime.today(),
        start_date=datetime(2013, 1, 1),
        end_date=datetime.today(),
    )

output = dcc.Graph(style={'width':'90vw',
                          'height':'50vw'},
                   id="graph")

app.layout = html.Div([
    dbc.Row(date_range_select),
    dbc.Row(output),
])

