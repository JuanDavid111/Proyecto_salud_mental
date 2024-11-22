import pandas as pd
import plotly.express as px

''' Definicion de la funcion que muestra la grafica de la severidad de los problemas mentales de las personas'''
def severidad_de_problemas_mentales( data_health: pd.DataFrame, query_reporte_problemas_mentales:str ) -> tuple:
    
    '''Se agrupan los datos por la persona reporto problemas mentales y por la severidad'''
    severidad_de_problemas_mentales = data_health.groupby(['Mental_Health_Condition','Severity'],dropna=False).size().reset_index().rename(columns={0: "Count_Severity"})
    
    '''Grafica de la severdad de los problemas mentales de las personas, con un query de si la persona reporto problemas mentales o no'''
    grafica_severidad_de_problemas_mentales = px.pie(severidad_de_problemas_mentales.query(f"Mental_Health_Condition == '{query_reporte_problemas_mentales}'"),values="Count_Severity", names="Severity", hole=.2, title="Severidad de los problemas mentales de las personas")
    texto_analisis = "La gráfica de pastel muestra que más de la mitad (51.8%) de las personas no presentan problemas mentales, mientras que el 16.9% tiene problemas de baja severidad, el 16.5% de severidad media y el 14.8% de alta severidad. Esto indica que, si bien la mayoría no tiene problemas mentales o son leves, una proporción importante (alrededor del 31%) experimenta dificultades de severidad media a alta."
    return (grafica_severidad_de_problemas_mentales, texto_analisis)
   

   
    