import pandas as pd
import plotly.express as px

''' Definicion de la funcion que muestra la grafica de la severidad de los problemas mentales de las personas'''
def severidad_de_problemas_mentales( data_health: pd.DataFrame, query_reporte_problemas_mentales:str ) -> tuple:
    
    '''Se agrupan los datos por la persona reporto problemas mentales y por la severidad'''
    severidad_de_problemas_mentales = data_health.groupby(['Mental_Health_Condition','Severity'],dropna=False).size().reset_index().rename(columns={0: "Count_Severity"})
    
    '''Grafica de la severdad de los problemas mentales de las personas, con un query de si la persona reporto problemas mentales o no'''
    grafica_severidad_de_problemas_mentales = px.pie(severidad_de_problemas_mentales.query(f"Mental_Health_Condition == '{query_reporte_problemas_mentales}'"),values="Count_Severity", names="Severity", hole=.2)

    texto_analisis_yes = "La gráfica de pastel muestra que menos de la mitad (51.8%) de las personas no presentan problemas mentales, mientras que el 16.9% tiene problemas de baja severidad, el 16.5% de severidad media y el 14.8% de alta severidad. Esto indica que, si bien la mayoría no tiene problemas mentales o son leves, una proporción importante (alrededor del 31%) experimenta dificultades de severidad media a alta."

    texto_analisis_no = "La gráfica de pastel muestra que menos de la mitad (48.2%) de las personas no presentan problemas mentales, mientras que el 18.4% tiene problemas de baja severidad, el 16.3% de severidad media y el 17.1% de alta severidad. Esto indica que, las personas que no reportaron tener ningun problema mental, suelen tener una condicion de las cuales no son concientes y puede llegar a ser grave."

    def_texto = lambda x: texto_analisis_yes if x == "Yes" else texto_analisis_no

    return (grafica_severidad_de_problemas_mentales, def_texto(query_reporte_problemas_mentales))
   

   
    