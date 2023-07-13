import dash
from dash import Dash, dcc, html, Input, Output, State, dash_table, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from datetime import *
from app import app
from data.dhs_data import *
import plotly.io as pio
from plotly.subplots import make_subplots
import numpy as np
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class MyApp(dash.Dash):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)

        # Set initial state in the constructor
        self.state = {
            "start_date": None,
            "end_date": None,
            "metric_values": None
        }

        # Move code with side effects to componentDidMount
        @self.callback(
            Output("graph", "figure"),
            Input("run-button", "n_clicks"),
            State("date-range", "start_date"),
            State("date-range", "end_date"),
            State("metric-dropdown", "value"),
        )
        def data_visualization(n_clicks, start_date, end_date, metric_values):
            if n_clicks in [0, None]:
                raise PreventUpdate

            # Apply date filter
            filtered_data = dhs_daily_df[
                (dhs_daily_df.index >= start_date) & (dhs_daily_df.index <= end_date)
            ]

            if not metric_values:
                raise ValueError("No metric value selected")

            # Set the template to 'plotly_dark'
            pio.templates.default = "plotly_dark"

            # Create the line chart
            fig = make_subplots()

            color_palette = ['sienna', 'orange', 'silver', 'purple', 'magenta', 'violet', 'wheat', 'coral', 'salmon', 'plum']

            if isinstance(metric_values, str):
                metric_values = [metric_values]  # Convert single metric value to a list

            for i, metric_value in enumerate(metric_values):
                if metric_value not in filtered_data.columns:
                    raise ValueError(f"Invalid metric value: {metric_value}")

                fig.add_trace(
                    go.Scatter(
                        x=filtered_data.index,
                        y=filtered_data[metric_value],
                        mode='markers+lines',
                        marker=dict(
                            color=color_palette[i % len(color_palette)],
                            size=2
                        ),
                        line=dict(
                            color=color_palette[i % len(color_palette)],
                            width=1
                        ),
                        name=metric_value,
                    )
                )

            # Customize the layout if needed
            fig.update_layout(
                title=dict(text="Daily Metrics"),
                xaxis=dict(title="Date"),
                xaxis_tickangle=0,
                yaxis=dict(title='Total Individuals', tickmode='auto', tickformat='d', range=[filtered_data[metric_values].min(), filtered_data[metric_values].max()]),
                legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='left', x=0),
                margin=dict(l=100, r=50, t=80, b=20),
                width=1050,
                height=500
            )

            return fig

        # Move code with side effects to componentDidMount
        @self.callback(
            Output("graph-2", "figure"),
            Input("run-button-2", "n_clicks"),
            State("date-range-2", "start_date"),
            State("date-range-2", "end_date"),
            State("metric-dropdown-2", "value"),
        )
        def data_visualization_2(n_clicks, start_date, end_date, metric_value):
            if n_clicks in [0, None]:
                raise PreventUpdate

            try:
                # Apply date filter
                filtered_data = dhs_daily_df[
                    (dhs_daily_df.index >= start_date) & (dhs_daily_df.index <= end_date)
                ]

                if metric_value not in filtered_data.columns:
                    raise ValueError(f"Invalid metric value: {metric_value}")

                # Set the template to 'plotly_dark'
                pio.templates.default = "plotly_dark"

                # Create the line chart
                fig = px.line(
                    filtered_data,
                    x=filtered_data.index,
                    y=metric_value,
                    color_discrete_sequence=['orange'],
                    labels=dict(
                        x='Date',
                        y='{}'.format(metric_value)
                    ),
                    title='Daily NYC Shelted Individuals'
                )

                # Customize the layout if needed
                fig.update_layout(
                    xaxis_tickangle=0,
                    legend=dict(orientation='h', yanchor='top', y=50, xanchor='left', x=0),
                    yaxis=dict(tickmode='auto', tickformat='d', range=[filtered_data[metric_value].min(), filtered_data[metric_value].max()]),
                    width=1500,
                    height=500
                )
                return fig

            except Exception as e:
                logging.error(str(e))

app = MyApp(__name__)

if __name__ == '__main__':
    app.run_server(debug=True)
