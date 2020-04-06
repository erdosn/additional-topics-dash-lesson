import dash
import pandas as pd
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output

df = pd.read_csv("data/iris.csv")
print(df.head())

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

input_box = dcc.Input(
    id="hello-world-input",
    placeholder='Enter a value...',
    type='text',
    value=''
)

options = [{"label": col, "value": col} for col in df.columns[:4]]
dropdown_x = dcc.Dropdown(
    id="x-axis-dropdown",
    options=options
)

dropdown_y = dcc.Dropdown(
    id="y-axis-dropdown",
    options=options
)



# This is where all the magic happens
app.layout = html.Div([
    html.H1("This is my cool App!"),
    # making a subheader
    input_box,
    html.Div(id="hello-world"),
    html.H3("X Axis"),
    dropdown_x,
    html.H3("Y Axis"),
    dropdown_y,
    html.Div(id="iris-graph"),
])


@app.callback(Output("hello-world", "children"),
              [Input("hello-world-input", "value")])
def render_header2(string):
    if string=="":
        string = "World"
    render_string = f"Hello {string}!"
    return html.H2(render_string)

# let's show some data
@app.callback(Output("iris-graph", "children"),
              [Input("x-axis-dropdown", "value"),
               Input("y-axis-dropdown", "value")])
def render_iris_scatter(x, y):
    if not x:
        x = "sepal length (cm)"
    if not y:
        y = "sepal width (cm)"
    trace = go.Scatter(x=df[x], y=df[y], mode='markers')
    fig = go.Figure(data=trace)
    iris_graph = dcc.Graph(figure=fig)
    return iris_graph



if __name__ == '__main__':
    app.run_server(debug=True)
