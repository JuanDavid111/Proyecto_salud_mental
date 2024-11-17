import pandas as pd

'''Ruta de el data set'''
file_data_path = './data/mental_health_dataset.csv'
data_health = pd.read_csv(file_data_path,sep=',')

data_health.head()