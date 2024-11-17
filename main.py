import pandas as pd

'''Ruta de el data set'''
file_data_path = './data/mental_health_dataset.csv'

'''Carga de datos del archivo cvs a python con pandas'''
data_health = pd.read_csv(file_data_path,sep=',')


print(data_health.head(10))