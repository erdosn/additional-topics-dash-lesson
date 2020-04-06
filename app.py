import dash
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server



##############
# App Layout Here
##############
app.layout = html.Div([
    html.H1("This is my App!"),
    html.Div(id="hello-world", children="hello world!")
])



if __name__ == '__main__':
    app.run_server(debug=True)
