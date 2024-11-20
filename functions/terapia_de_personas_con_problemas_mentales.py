import pandas as pd
import plotly.express as px

'''Grafica de las personas que reportaron problemas mentales y las que no, de si han ido a terapia o no'''
def terapia_de_personas_con_problemas_mentales (data_health: pd.DataFrame):
    '''Se agrupan los datos si la persona reporto problemas mentales y si fue a terapia'''
    terapia_personas = data_health.groupby(['Mental_Health_Condition','Consultation_History']).size().reset_index().rename(columns={0: "Count_Consultatuion_History"})

    '''Grafica si las personas fueron a terapia dependiendo de su condicion mental'''
    px.pie(terapia_personas.query(f"Mental_Health_Condition == '{'Yes'}'"),values="Count_Consultatuion_History", names="Consultation_History", hole=.2, title="Las personas que han ido a terapia")