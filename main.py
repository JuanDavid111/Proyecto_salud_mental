import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html
from functions import severidad_de_problemas_mentales


'''Ruta de el data set'''
file_data_path = './data/mental_health_dataset.csv'

'''Carga de datos del archivo cvs a python con pandas'''
data_health = pd.read_csv(file_data_path,sep=',')


severidad_de_problemas_mentales(data_health,"Yes")


''' Parte de la interfaz grafica'''
# external_stylesheets = [dbc.themes.BOOTSTRAP]
# app = Dash(__name__,external_stylesheets=external_stylesheets)

# select = dbc.Select(
#     id="select",
#     options=[
#         {"label": "Yes", "value": "Yes"},
#         {"label": "No", "value": "No"},
        
#     ],
# )

# app.layout = dbc.Container(
#     [
#         html.H1("Graficas"),
#         html.Hr(),
#         dbc.Row(
#             [
#                 dbc.Col([dcc.Graph(id="Grafico_Prueba"),select]),
#                 dbc.Col([html.H2("hola")])
               
#             ]
#         ),
       
#     ]
# )

# @app.callback(
#         Output(component_id="Grafico_Prueba",component_property="figure"),
#         Input(component_id="select",component_property="value")
# )
# def update_graph(values):
#     return sev.severidad_de_problemas_mentales(data_health,query_reporte_problemas_mentales=values)

# if __name__ == '__main__':
#     app.run(debug=True)
    
