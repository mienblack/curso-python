import pandas as pd
import openpyxl
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import plotly.express as px


# Inicializa o app
app = Dash(__name__)

# Executar o dataframe
df = pd.read_excel("data/Vendas.xlsx", engine='openpyxl')

# Criar o gráfico
fig = px.bar(df, x=["a", "b", "c"], y=[1, 3, 2])

# Cria o Layout do dashboard
app.layout = html.Div([
    html.H4('Interactive color selection with simple Dash example'),
    html.P("Select color:"),
    dcc.Dropdown(
        id="dropdown",
        options=['Gold', 'MediumTurquoise', 'LightGreen'],
        value='Gold',
        clearable=False,
    ),
    dcc.Graph(
        id="graph",
        figure = fig
        )
])

# Roda o app
if __name__ == '__main__':
    app.run_server(debug=True)
