from dash import Dash, html, dcc, Input, Output
from covid import choro, scatt, pie, sun, bar, box, line, hist, area

# Initialize Dash App
app = Dash(__name__)

# Layout
app.layout = html.Div(
    style={"backgroundColor": "#001f3f", "color": "white"},
    children=[
        # Title
        html.H1("COVID-19 Dashboard", style={"textAlign": "center", "color": "white"}),

        # Section 1: Dropdown for Maps
        html.Div([
            html.H3("Select a Map:", style={"textAlign": "center"}),
            dcc.Dropdown(
                id="map-dropdown",
                options=[
                    {"label": "Choropleth Map", "value": "choropleth"},
                    {"label": "Bubble Map", "value": "bubble"}
                ],
                value="choropleth",
                style={
                    "margin": "0 auto",
                    "width": "50%",
                    "backgroundColor": "white",
                    "color": "#9dc8d4"
                }
            ),
            dcc.Graph(id="map-graph")
        ]),

        # Section 2: Dropdown for Pie Chart and Sunburst
        html.Div([
            html.H3("Select a Chart:", style={"textAlign": "center"}),
            dcc.Dropdown(
                id="chart-dropdown",
                options=[
                    {"label": "Pie Chart", "value": "pie"},
                    {"label": "Sunburst Chart", "value": "sunburst"}
                ],
                value="pie",
                style={
                    "margin": "0 auto",
                    "width": "50%",
                    "backgroundColor": "#001f3f",
                    "color": "white"
                }
            ),
            dcc.Graph(id="chart-graph")
        ]),

        # Section 3: Dropdown for Distribution Visualization
        html.Div([
            html.H3("Select a Distribution Visualization:", style={"textAlign": "center"}),
            dcc.Dropdown(
                id="dist-dropdown",
                options=[
                    {"label": "Top 10 Countries", "value": "bar"},
                    {"label": "Death Rate Distribution", "value": "boxplot"},
                    {"label": "Distribution of Cases", "value": "hist"}
                ],
                value="bar",
                style={
                    "margin": "0 auto",
                    "width": "50%",
                    "backgroundColor": "#001f3f",
                    "color": "white"
                }
            ),
            dcc.Graph(id="dist-graph")
        ]),

        # Footer Section: Line Chart and Area Chart
        html.Div([
            html.H3("Line and Area Charts", style={"textAlign": "center"}),
            dcc.Graph(figure=line),
            dcc.Graph(figure=area)
        ])
    ]
)

# Callbacks 
@app.callback(
    Output("map-graph", "figure"),
    Input("map-dropdown", "value")
)
def update_map(selected_map):
    if selected_map == "choropleth":
        return choro
    elif selected_map == "bubble":
        return scatt

@app.callback(
    Output("chart-graph", "figure"),
    Input("chart-dropdown", "value")
)
def update_chart(selected_chart):
    if selected_chart == "pie":
        return pie
    elif selected_chart == "sunburst":
        return sun

@app.callback(
    Output("dist-graph", "figure"),
    Input("dist-dropdown", "value")
)
def update_distribution(selected_dist):
    if selected_dist == "bar":
        return bar
    elif selected_dist == "boxplot":
        return box
    elif selected_dist == "hist":
        return hist
choro.update_layout(
    paper_bgcolor="#001f3f",  # Matches dashboard background
    plot_bgcolor="#001f3f",  # Matches dashboard background
    font_color="white"       )
scatt.update_layout(
    paper_bgcolor="#001f3f",  # Matches dashboard background
    plot_bgcolor="#001f3f",  # Matches dashboard background
    font_color="white"       )
pie.update_layout(
    paper_bgcolor="#001f3f",  # Matches dashboard background
    plot_bgcolor="#001f3f",  # Matches dashboard background
    font_color="white"       )
bar.update_layout(
    paper_bgcolor="#001f3f",  # Matches dashboard background
    plot_bgcolor="#001f3f",  # Matches dashboard background
    font_color="white"       )
hist.update_layout(
    paper_bgcolor="#001f3f",  # Matches dashboard background
    plot_bgcolor="#001f3f",  # Matches dashboard background
    font_color="white"       )
box.update_layout(
    paper_bgcolor="#001f3f",  # Matches dashboard background
    plot_bgcolor="#001f3f",  # Matches dashboard background
    font_color="white"       )
line.update_layout(
    paper_bgcolor="#001f3f",  # Matches dashboard background
    plot_bgcolor="#001f3f",  # Matches dashboard background
    font_color="white"       )
area.update_layout(
    paper_bgcolor="#001f3f",  # Matches dashboard background
    plot_bgcolor="#001f3f",  # Matches dashboard background
    font_color="white"       )
sun.update_layout(
    paper_bgcolor="#001f3f",  # Matches dashboard background
    plot_bgcolor="#001f3f",  # Matches dashboard background
    font_color="white"       )

# Run the App
if __name__ == "__main__":
    app.run_server(debug=True)

