import pandas as pd
import plotly.express as px

'''Grafica de las personas que reportaron problemas mentales y las que no, de si han ido a terapia o no'''
def terapia_de_personas_con_problemas_mentales (data_health: pd.DataFrame, query_reporte_problemas_mentales:str):
    '''Se agrupan los datos si la persona reporto problemas mentales y si fue a terapia'''
    terapia_personas = data_health.groupby(['Mental_Health_Condition','Consultation_History']).size().reset_index().rename(columns={0: "Count_Consultatuion_History"})

    '''Grafica si las personas fueron a terapia dependiendo de su condicion mental'''
    grafica_terapia_personas = px.pie(terapia_personas.query(f"Mental_Health_Condition == '{query_reporte_problemas_mentales}'"),values="Count_Consultatuion_History", names="Consultation_History", hole=.2, title="Las personas que han ido a terapia")

    

    texto_analisis = query_reporte_problemas_mentales == 'Yes' if 'La gráfica sugiere que una proporción significativa de personas con problemas de salud mental no ha asistido a terapia, lo que indica una necesidad de abordar las barreras que impiden el acceso a estos servicios.' else 'La gráfica sugiere que un número significativo de personas sin problemas de salud mental diagnosticados asisten a terapia, lo que subraya la importancia de la terapia como una herramienta para el bienestar general.'

    return (grafica_terapia_personas, grafica_terapia_personas)