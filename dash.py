import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)

# Synthetic data for scatter plot
data_scatter = pd.DataFrame({
    "GDP": np.random.randint(500, 50000, 100),
    "Life Expectancy": np.random.uniform(50, 85, 100),
    "Country": [f"Country {i}" for i in range(1, 101)]
})

# Synthetic data for bar plot
data_bar = pd.DataFrame({
    "Country": [f"Country {i}" for i in range(1, 21)],
    "Population": np.random.randint(1000000, 100000000, 20)
})

# Create synthetic graphs
fig1 = px.scatter(data_scatter, x="GDP", y="Life Expectancy", hover_name="Country",
                  title="Synthetic GDP vs Life Expectancy", labels={"GDP": "GDP", "Life Expectancy": "Life Expectancy"})

fig2 = px.bar(data_bar, x="Country", y="Population", title="Synthetic Population of Countries",
              labels={"Country": "Country", "Population": "Population"})

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

# Sidebar layout
sidebar = html.Div(
    [
        html.Hr(),
        dbc.Button("GDP vs Life Expectancy", href="/", id="page-1-link", color="primary", className="mb-2"),
        dbc.Button("Population", href="/page-2", id="page-2-link", color="secondary", className="mb-2"),
    ],
    style={
        'width': '15%',
        'position': 'fixed',
        'top': '0',
        'right': '0',
        'height': '100%',
        'backgroundColor': '#343a40',
        'padding': '10px',
        'z-index': '10',
        'display': 'flex',
        'flexDirection': 'column',
        'alignItems': 'center'
    }
)

# Content layout
content = html.Div(id="page-content", style={
    'margin-right': '15%',
    'padding': '10px',
    'margin-top': '40px'
})

# Define the layout
app.layout = html.Div([
    dcc.Location(id='url'),
    sidebar,
    content
])

# Define the content for each page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/" or pathname == "/page-1":
        return html.Div([
            html.H2("GDP vs Life Expectancy (Synthetic Data)"),
            dcc.Graph(figure=fig1)
        ])
    elif pathname == "/page-2":
        return html.Div([
            html.H2("Population of Countries (Synthetic Data)"),
            dcc.Graph(figure=fig2)
        ])
    else:
        return "404 - Page not found"

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
