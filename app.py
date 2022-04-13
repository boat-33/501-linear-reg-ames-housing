import dash
from dash import dcc,html
from dash.dependencies import Input, Output, State


########### Styling colors
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

########### Define your variables ######
myheading1='Predicting Home Sale Prices in Ames, Iowa'
image1='ames_welcome.jpeg'
tabtitle = 'Housing Price Predictions'
sourceurl = 'http://jse.amstat.org/v19n3/decock.pdf'
githublink = 'https://github.com/boat-33/501-linear-reg-ames-housing'


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children=myheading1, style={'textAlign': 'center', 'color': colors['text']}),
    html.Div([
        html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto', 'paddingLeft': '20px'}, className='four columns'),
        html.Div([
                html.H3(children='Features of Home:', style={'textAlign': 'left', 'color': colors['text']}),
                html.Div('Year Built:', style={'textAlign': 'left', 'color': colors['text']}),
                dcc.Input(id='YearBuilt', value=2010, type='number', min=2006, max=2010, step=1),
                html.Div(children='Bathrooms:', style={'textAlign': 'left', 'color': colors['text']}),
                dcc.Input(id='Bathrooms', value=2, type='number', min=1, max=5, step=1),
                html.Div(children='Bedrooms:', style={'textAlign': 'left', 'color': colors['text']}),
                dcc.Input(id='BedroomAbvGr', value=4, type='number', min=1, max=5, step=1),
                html.Div(children='Total Square Feet:', style={'textAlign': 'left', 'color': colors['text']}),
                dcc.Input(id='TotalSF', value=2000, type='number', min=100, max=5000, step=1),
                html.Div(children='Single Family Home:', style={'textAlign': 'left', 'color': colors['text']}),
                dcc.Input(id='SingleFam', value=0, type='number', min=0, max=1, step=1),
                html.Div(children='Large Neighborhood:', style={'textAlign': 'left', 'color': colors['text']}),
                dcc.Input(id='LargeNeighborhood', value=0, type='number', min=0, max=1, step=1),
                html.Div(children='Garage Cars:', style={'textAlign': 'left', 'color': colors['text']}),
                dcc.Input(id='GarageCars', value=0, type='number', min=0, max=12, step=1)

            ], className='four columns'),
            html.Div([
                html.Button(children='Submit', id='submit-val', n_clicks=0,
                                style={
                                'background-color': 'red',
                                'color': 'white',
                                'margin-left': '5px',
                                'verticalAlign': 'center',
                                'horizontalAlign': 'center'}
                                ),
                html.H3('Predicted Home Value:', style={'textAlign': 'left', 'color': colors['text']}),
                html.Div(id='Results', style={'textAlign': 'left', 'color': colors['text']})
            ], className='four columns')
        ], className='twelve columns',
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4('Regression Equation:', style={'textAlign': 'left', 'color': colors['text'], 'paddingLeft': '20px'}),
    html.Div(children='Predicted Price = (- $1,360.5K Baseline) + ($0.7K * Year Built) + ($12.7K * Bathrooms) + (- $7.7K * Bedrooms) + ($0.049K * Total Square Feet) + ($ 24.2K * Single Family Home) + (- $7.5 K * Large Neighborhood) +  + ($ 19.8 K * GarageCars)', style={'textAlign': 'left', 'color': colors['text'], 'paddingLeft': '20px'}),
    html.Br(),
    html.A('Google Spreadsheet', href='https://docs.google.com/spreadsheets/d/1q2ustRvY-GcmPO5NYudvsBEGNs5Na5p_8LMeS4oM35U/edit?usp=sharing', style={'paddingLeft': '20px'}),
    html.Br(),
    html.A('Code on Github', href=githublink, style={'paddingLeft': '20px'}),
    html.Br(),
    html.A("Data Source", href=sourceurl, style={'paddingLeft': '20px'}),
    ]
)


######### Define Callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='YearBuilt', component_property='value'),
    State(component_id='Bathrooms', component_property='value'),
    State(component_id='BedroomAbvGr', component_property='value'),
    State(component_id='TotalSF', component_property='value'),
    State(component_id='SingleFam', component_property='value'),
    State(component_id='LargeNeighborhood', component_property='value'),
    State(component_id='GarageCars', component_property='value')

)
def ames_lr_function(clicks, YearBuilt,Bathrooms,BedroomAbvGr,TotalSF,SingleFam,LargeNeighborhood,GarageCars):
    if clicks==0:
        return "waiting for inputs"
    else:
        y = [-1040627.9366 + 533.975*YearBuilt + 10105.0483*Bathrooms + -6632.5676*BedroomAbvGr + 43.6881*TotalSF+ 24186.0274*SingleFam+ -7536.3808*LargeNeighborhood + 19855.1213*GarageCars]
        formatted_y = "${:,.2f}".format(y[0])
        return formatted_y



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
