from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/sales_file.csv")

app = Dash(__name__)

fig = px.line(df, x="date", y="sales")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsels Sales Graph', style={'textAlign':'center'}),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)