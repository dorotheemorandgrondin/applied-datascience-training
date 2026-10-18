# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX launch data into a pandas dataframe
# (download it first with:
#  wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

site_options = [{'label': 'All Sites', 'value': 'ALL'}] + [
    {'label': site, 'value': site} for site in sorted(spacex_df['Launch Site'].unique())
]

# Create an app layout
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),

    # TASK 1: Add a dropdown list to enable Launch Site selection
    dcc.Dropdown(id='site-dropdown',
                 options=site_options,
                 value='ALL',
                 placeholder='Select a Launch Site here',
                 searchable=True),
    html.Br(),

    # TASK 2: Add a pie chart to show the total successful launches count for all sites
    # If a specific launch site was selected, show the Success vs. Failed counts for the site
    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    # TASK 3: Add a slider to select payload range
    dcc.RangeSlider(id='payload-slider',
                    min=0, max=10000, step=1000,
                    marks={i: str(i) for i in range(0, 10001, 2500)},
                    value=[min_payload, max_payload]),

    # TASK 4: Add a scatter chart to show the correlation between payload and launch success
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


# TASK 2: callback for the pie chart
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        fig = px.pie(spacex_df[spacex_df['class'] == 1], names='Launch Site',
                     title='Total Successful Launches by Site')
    else:
        filtered = spacex_df[spacex_df['Launch Site'] == entered_site]
        counts = filtered['class'].value_counts().reset_index()
        counts.columns = ['class', 'count']
        counts['class'] = counts['class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(counts, values='count', names='class',
                     title=f'Total Success vs. Failed Launches for site {entered_site}')
    return fig


# TASK 4: callback for the scatter chart
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id='payload-slider', component_property='value')])
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    filtered = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)]
    title = 'Correlation between Payload and Success for all Sites'
    if entered_site != 'ALL':
        filtered = filtered[filtered['Launch Site'] == entered_site]
        title = f'Correlation between Payload and Success for {entered_site}'
    fig = px.scatter(filtered, x='Payload Mass (kg)', y='class',
                     color='Booster Version Category', title=title)
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=False)
