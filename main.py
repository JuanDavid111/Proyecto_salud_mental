import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html
from functions import top_5_paises_salud_mental, top_10_profesiones_peor_salud_mental

from functions.salud_mental_por_edad import salud_mental_edades
from functions.salud_mental_genero import salud_mental_genero
from functions.salud_mental_por_nivel_de_estres import salud_mental_por_nivel_de_estres
from functions.severidad_de_problemas_mentales import severidad_de_problemas_mentales
from functions.terapia_de_personas_con_problemas_mentales import terapia_de_personas_con_problemas_mentales
from functions.tiempo_de_sleep import nivel_de_estres_tiempo_sueño, salud_mental_tiempo_sueño
from functions.salud_profesiones import analisis_por_profesion



'''Ruta de el data set'''
file_data_path = './data/mental_health_dataset.csv'

'''Carga de datos del archivo cvs a python con pandas'''
data_health = pd.read_csv(file_data_path,sep=',')

'''Llamar funciones'''


top_5_fig, text_top_5 = top_5_paises_salud_mental(data_health)
top_10_profesiones_fig, text_top_10 = top_10_profesiones_peor_salud_mental(data_health)




''' Parte de la interfaz grafica'''
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__,external_stylesheets=external_stylesheets)

select = dbc.Select(
    id="select",
    options=[
        {"label": "Yes", "value": "Yes"},
        {"label": "No", "value": "No"},
        
    ],
)


slice = dbc.Carousel(
    id='Carousel',
    items=[
        {"key": "1", "src": "./assets/top_10_grafica.png", "img_style" : {"height" : '80%' , "width" : "50%"} },
        {"key": "2", "src": "./assets/top_5_grafica.png", "img_style" : {"height" : '50vh' , "width" : "50vw"}},
    ],
    
    controls=True,
    indicators=False,
    interval=5000,
    ride="carousel",
)

div_carousel = html.Div(children=[
    dbc.Row(
            [
                slice
            ]
        )
    ],
    style={ "padding": "20px", "border-radius": "15px", "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.2)", "margin-bottom": "20px"}    
)

div_edades = html.Div(children=[
        dbc.Card([
                dbc.CardHeader([html.H2('Edades y Salud Mental')]),
                dbc.CardImg(id='salud_mental_edad'),
                dbc.CardBody([
                    
                    html.P(className="card-text",id='texto_salud_mental_edad')
                    ]
                )
            ],
            style={"width": "40vw"}
        )
    ],
    
    style={ "padding": "20px", "border-radius": "15px", "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.2)", "margin-bottom": "20px"}   
)
div_genero = html.Div(children=[
        dbc.Card([
                dbc.CardHeader([html.H2('Género y Salud Mental')]),
                dcc.Graph(id='salud_mental_genero'),
                dbc.CardBody([
                    html.P(className="card-text",id='texto_salud_mental_genero')
                    ]
                )
            ],
            # style={"width": "30vw"}
        )
    ],
    
    style={ "padding": "20px", "border-radius": "15px", "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.2)", "margin-bottom": "20px"}   
)

div_salud_por_nivel_de_estres = html.Div(children=[
        dbc.Card([
                dbc.CardHeader([html.H2('Nivel de Estrés')]),
                dbc.CardImg(id='salud_mental_por_nivel_de_estres'),
                dbc.CardBody([
                    html.P(className="card-text",id='texto_salud_mental_por_nivel_de_estres')
                    ]
                )
            ],
            style={"width": "40vw"}
        )
    ],
    
    style={ "padding": "20px", "border-radius": "15px", "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.2)", "margin-bottom": "20px"}   
)

div_severidad = html.Div(children=[
        dbc.Card([
                dbc.CardHeader([html.H2('Gravedad de problemas mentales en las personas' )]),
                dcc.Graph(id='severidad_de_problemas_mentales'),
                dbc.CardBody([
                    html.P(className="card-text",id='texto_severidad_de_problemas_mentales'),
                    html.H5("Reporto Problema Mental:", style={'margin-bottom': '30px'}),
                    dcc.Dropdown(id='severidad_de_problemas_mentales_query',
                        options=['Yes', 'No'],
                        value='Yes', clearable=False
                    )
                    ]
                )
            ],
            # style={"width": "30vw"}
        )
    ],
    
    style={ "padding": "20px", "border-radius": "15px", "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.2)", "margin-bottom": "20px"}   
)
div_terapia = html.Div(children=[
        dbc.Card([
                dbc.CardHeader([html.H2('Personas en Terapia y Problemas Mentales')]),
                dcc.Graph(id='terapia_de_personas_con_problemas_mentales'),
                dbc.CardBody([
                    html.P(className="card-text",id='texto_terapia_de_personas_con_problemas_mentales'),
                    html.H5("Reporto Problema Mental:", style={'margin-bottom': '30px'}),
                    dcc.Dropdown(id='terapia_de_personas_con_problemas_mentales_query',
                        options=['Yes', 'No'],
                        value='Yes', clearable=False
                    )
                    ]
                )
            ],
            # style={"width": "30vw"}
        )
    ],
    
    style={ "padding": "20px", "border-radius": "15px", "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.2)", "margin-bottom": "20px"}   
)

div_nivel_de_estres_tiempo_sueño = html.Div(children=[
        dbc.Card([
                dbc.CardHeader([html.H2('Nivel de Estrés con el tiempo de sueño')]),
                dbc.CardImg(id='nivel_de_estres_tiempo_sueño'),
                dbc.CardBody([
                    html.P(className="card-text",id='texto_nivel_de_estres_tiempo_sueño')
                    ]
                )
            ],
            style={"width": "40vw"}
        )
    ],
    
    style={ "padding": "20px", "border-radius": "15px", "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.2)", "margin-bottom": "20px"}   
)
div_salud_mental_tiempo_sueño = html.Div(children=[
        dbc.Card([
                dbc.CardHeader([html.H2('Salud Mental con el tiempo de sueño')]),
                dbc.CardImg(id='salud_mental_tiempo_sueño'),
                dbc.CardBody([
                    html.P(className="card-text",id='texto_salud_mental_tiempo_sueño')
                    ]
                )
            ],
            style={"width": "40vw"}
        )
    ],
    
    style={ "padding": "20px", "border-radius": "15px", "box-shadow": "0 4px 10px rgba(0, 0, 0, 0.2)", "margin-bottom": "20px"}   
)


app.layout = dbc.Container(
    children=[
        html.H1("Analisis Salud Mental"),
        html.Hr(),
        dbc.Row([
            dbc.Col([div_carousel])

        ]),
        dbc.Row([
            dbc.Col([div_edades]),
            dbc.Col([div_genero]),
        ]),

        dbc.Row([
            dbc.Col([div_salud_por_nivel_de_estres]),
            dbc.Col([div_severidad]),
        ]),
        dbc.Row([
            dbc.Col([div_nivel_de_estres_tiempo_sueño]),
            dbc.Col([div_terapia])
        ]),
        dbc.Row([
            dbc.Col([div_salud_mental_tiempo_sueño],style={'text-aling': 'center', 'justify-content': 'center'}),
        ])
        
    ],
    style={"height" : '70vh' , "width" : "150vw", 'text-align': 'center'}
)

@app.callback(
    Output(component_id='salud_mental_edad',component_property='src'),
    Output('texto_salud_mental_edad',component_property='children'),
    Input('salud_mental_edad',component_property='src')
)
def make_graph(col):
    path_grafica_salud_edades ,mm= salud_mental_edades(data_health)
    return path_grafica_salud_edades, mm


@app.callback(
    Output(component_id='salud_mental_genero',component_property='figure'),
    Output('texto_salud_mental_genero',component_property='children'),
    Input('salud_mental_genero',component_property='figure')
)
def make_graph(col):
    path_grafica_salud_mental_genero ,mm= salud_mental_genero(data_health)
    return path_grafica_salud_mental_genero, mm

@app.callback(
    Output(component_id='salud_mental_por_nivel_de_estres',component_property='src'),
    Output('texto_salud_mental_por_nivel_de_estres',component_property='children'),
    Input('salud_mental_por_nivel_de_estres',component_property='src')
)
def make_graph(col):
    path_grafica_salud_mental_por_nivel_de_estres ,mm= salud_mental_por_nivel_de_estres(data_health)
    return path_grafica_salud_mental_por_nivel_de_estres, mm


@app.callback(
    Output(component_id='severidad_de_problemas_mentales',component_property='figure'),
    Output('texto_severidad_de_problemas_mentales',component_property='children'),
    Input('severidad_de_problemas_mentales_query',component_property='value')
)
def make_graph(query):
    path_grafica_severidad_de_problemas_mentales ,mm= severidad_de_problemas_mentales(data_health,query)
    return path_grafica_severidad_de_problemas_mentales, mm
@app.callback(
    Output(component_id='terapia_de_personas_con_problemas_mentales',component_property='figure'),
    Output('texto_terapia_de_personas_con_problemas_mentales',component_property='children'),
    Input('terapia_de_personas_con_problemas_mentales_query',component_property='value')
)
def make_graph(query):
    path_grafica_terapia_de_personas_con_problemas_mentales ,mm= terapia_de_personas_con_problemas_mentales(data_health,query)
    return path_grafica_terapia_de_personas_con_problemas_mentales, mm

@app.callback(
    Output(component_id='nivel_de_estres_tiempo_sueño',component_property='src'),
    Output('texto_nivel_de_estres_tiempo_sueño',component_property='children'),
    Input('nivel_de_estres_tiempo_sueño',component_property='src')
)
def make_graph(col):
    path_grafica_nivel_de_estres_tiempo_sueño ,mm= nivel_de_estres_tiempo_sueño(data_health)
    return path_grafica_nivel_de_estres_tiempo_sueño, mm

@app.callback(
    Output(component_id='salud_mental_tiempo_sueño',component_property='src'),
    Output('texto_salud_mental_tiempo_sueño',component_property='children'),
    Input('salud_mental_tiempo_sueño',component_property='src')
)
def make_graph(col):
    path_grafica_nivel_de_estres_tiempo_sueño ,mm= salud_mental_tiempo_sueño(data_health)
    return path_grafica_nivel_de_estres_tiempo_sueño, mm









if __name__ == '__main__':
    app.run(debug=True)
    
