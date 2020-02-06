import dash_core_components as dcc
import dash_html_components as html


def make_name_field(title="First Name"):
    id = title.lower().replace(" ", "_") + "_field"
    input_name_field = dcc.Input(
        id = id,
        placeholder=f"{title}",
        type='text',
        value=''
    )
    input_name_component = html.Div([
        input_name_field
    ])
    return input_name_component


first_name_components = make_name_field(title="First Name")
last_name_components = make_name_field(title="Last Name")
