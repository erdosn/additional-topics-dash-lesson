import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


from components.NameFields import first_name_components, last_name_components

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

top_markdown_text = '''
# My First Form
(this app brought to you by erdosn)

-----
'''

def update_output(first_name_field, last_name_field):
    return u'Input 1 {}  and Input 2 {}'.format(first_name_field, last_name_field)



##############
# App Layout Here
##############
app.layout = html.Div([
    dcc.Markdown(children=top_markdown_text),
    first_name_components,
    last_name_components,
    html.Div(id="hello-world", children="hello world!"),
    dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': [1, 2, 3, 4],
                    'y': [4, 1, 3, 5],
                    'name': 'Trace 1',
                    'mode': 'markers',
                    'marker': {'size': 12}
                }
            ],
            'layout': {
                'clickmode': 'event+select'
            }
        }
    )
])


@app.callback(
    Output(component_id='hello-world', component_property='children'),
    [Input(component_id='first_name_field', component_property='value'),
     Input(component_id='last_name_field', component_property='value')]
)
def hello_person(first_name=None, last_name=None):
    if first_name or last_name:
        first_name = first_name if first_name else ""
        last_name = last_name if last_name else ""
        text = "hello {} {}!!!!!!".format(first_name, last_name)
    else:
        text = "hello world!"

    hello_person_component = html.Div(
        id="hello-world",
        children=text
    )
    return hello_person_component


@app.callback(
    Output(component_id='basic-interactions', component_property='figure'),
    [Input(component_id='first_name_field', component_property='value')]
)
def update_basic_interactions(n_points):
    n_points = int(n_points)
    x = np.random.randint(0, 10, n_points)
    y = np.random.randint(0, 10, n_points)
    figure_component = dcc.Graph(
        id='basic-interactions',
        figure={
            'data': [
                {
                    'x': x,
                    'y': y,
                    'name': 'Trace 1',
                    'mode': 'markers',
                    'marker': {'size': 12}
                }
            ],
            'layout': {
                'clickmode': 'event+select'
            }
        }
    )
    return figure_component

if __name__ == '__main__':
    app.run_server(debug=True)
