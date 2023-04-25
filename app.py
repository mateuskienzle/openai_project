import dash_bootstrap_components as dbc
import dash
from dash_bootstrap_templates import load_figure_template

# estilos = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css", "https://fonts.googleapis.com/icon?family=Material+Icons"]
load_figure_template("solar")

app = dash.Dash(external_stylesheets = [dbc.themes.SOLAR])

app.scripts.config.serve_locally = True
server = app.server