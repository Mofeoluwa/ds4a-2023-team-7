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
from app import app
from data.dhs_data import *
from datetime import *

@app.callback(
    Output("graph", "figure"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date")
)
def data_visualization(start_date, end_date):

    # Apply date filter
    filtered_data = dhs_daily_df[
        (dhs_daily_df.index >= start_date) & (dhs_daily_df.index <= end_date)
    ]

    # Set the template to 'plotly_dark'
    pio.templates.default = "plotly_dark"

    # Create the line chart
    fig = px.line(
        filtered_data,
        x=filtered_data.index,
        y='total_individuals_in_shelter',
        color_discrete_sequence=['orange'],
        labels=dict(
            x='Date',
            y='Total Sheltered Individuals'
        ),
        title='Daily Total Individuals in NYC Shelters'
    )

    # Customize the layout if needed
    fig.update_layout(
        xaxis_tickangle=0,
        legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='left', x=0),
        yaxis=dict(tickmode='auto', tickformat='d', range=[40000, filtered_data['total_individuals_in_shelter'].max()]),
        margin=dict(l=100, r=50, t=80, b=20),  # Adjust the left and right margin values as desired
        width=1500,  # Set the desired width of the figure
        height=500  # Set the desired height of the figure
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)