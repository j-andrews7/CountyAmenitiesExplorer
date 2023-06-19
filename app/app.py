from shiny import App, reactive, ui
from shinywidgets import output_widget, register_widget
from pathlib import Path
import json
import pandas as pd
import plotly.express as px

# Get county fips data.
f = open(Path(__file__).parent / 'data/geojson-counties-fips.json')
counties = json.load(f)
f.close()

df = pd.read_csv(Path(__file__).parent / "data/fips-unempl-16.csv",
                   dtype={"fips": str})

app_ui = ui.page_fluid(
    ui.tags.h1("County Ammenities Explorer"),
    output_widget("map"),
)


def server(input, output, session):
    fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'unemp':'unemployment rate'}
                          )
    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, width=1400, height=800)

    register_widget("map", fig)

app = App(app_ui, server)
