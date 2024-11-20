import pandas as pd
from functions import severidad_de_problemas_mentales

'''Ruta de el data set'''
file_data_path = './data/mental_health_dataset.csv'

'''Carga de datos del archivo cvs a python con pandas'''
data_health = pd.read_csv(file_data_path,sep=',')



