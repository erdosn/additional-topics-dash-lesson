import dash
import dash_core_components as dcc
import dash_html_components as html

from components.NameFields import first_name_components, last_name_components

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

top_markdown_text = '''
### My First Form
'''

app.layout = html.Div([

    dcc.Markdown(children=top_markdown_text),
    first_name_components,
    last_name_components

])

def update_output(first_name_field, last_name_field):
    return u'Input 1 {}  and Input 2 {}'.format(first_name_field, last_name_field)


if __name__ == '__main__':
    app.run_server(debug=True)
