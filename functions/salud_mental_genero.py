import pandas as pd
import plotly.express as px


def salud_mental_genero(dataset: pd.DataFrame) -> tuple:
    

    mascara1 = ((dataset['Gender'] == "Female") & (dataset['Mental_Health_Condition'] == "Yes"))
    primer_rango = dataset[mascara1]    

    mascara2 = ((dataset['Gender'] == "Male") & (dataset['Mental_Health_Condition'] == "Yes"))
    segundo_rango = dataset[mascara2]  


    mascara3 = ((dataset['Gender'] == "Non-binary") & (dataset['Mental_Health_Condition'] == "Yes"))
    tercer_rango = dataset[mascara3]  

    mascara4 = ((dataset['Gender'] == "Prefer not to say") & (dataset['Mental_Health_Condition'] == "Yes"))
    cuarto_rango = dataset[mascara4]    

    # se convierte a diccionario para hacer la gráfica
    diccionario_aux = {
        'Female': primer_rango.shape[0],
        'Male': segundo_rango.shape[0],
        'Non-binary': tercer_rango.shape[0],
        'Prefer not to say': cuarto_rango.shape[0]
    }
    df_pie = pd.DataFrame(list(diccionario_aux.items()), columns=['Gender', 'Count']) # hay que convertirlo en dataset para que el gráfico funcione

    df = px.data.tips()
    fig = px.pie(df_pie, values='Count', names='Gender',  color_discrete_sequence=px.colors.sequential.RdBu)
    texto_analisis = "El análisis comparativo revela que tanto las mujeres como las personas no-binarias tienen una alta incidencia de problemas de salud mental, cada uno con sus propios desafíos únicos. Las mujeres enfrentan estrés y ansiedad debido a roles y expectativas sociales.Por otro lado, las personas no-binarias sufren discriminación, estigma y falta de apoyo social."
    return (fig, texto_analisis)
