import pandas as pd
import matplotlib.pyplot as plt


def salud_mental_por_pais(df: pd.DataFrame, query_reporta_problemas) -> tuple:



    # Suponiendo que tu DataFrame se llama 'df'

    # Agrupamos los datos por país y contamos los diagnósticos 'Yes'
    conteo_por_pais = df.groupby('Country')['Mental_Health_Condition'].value_counts().unstack(fill_value=0)
    print(conteo_por_pais)


    # Filtrar los datos donde diagnóstico es "Yes"
    df_yes = df[df['Mental_Health_Condition'] == f'{query_reporta_problemas}']

    # Agrupar por país y contar los "Yes"
    conteo_por_pais = df_yes['Country'].value_counts()

    # Crear el gráfico de torta
    plt.pie(conteo_por_pais, labels=conteo_por_pais.index, autopct='%1.1f%%')
    plt.title('Porcentaje de "Yes" por país')
    plt.show()
    texto_analisis = "El análisis del gráfico muestra que Estados Unidos lidera en términos de prevalencia de problemas de salud mental, seguido de cerca por India y Canadá. Los altos niveles de estrés, las barreras para acceder a servicios de salud mental y el estigma social son factores comunes que afectan a estos países."
    return (plt.figure(),texto_analisis)


def top_5_paises_salud_mental(df: pd.DataFrame) -> tuple:
    mascara = df['Mental_Health_Condition'] == 'Yes'

    filtro = df[mascara]

    count_paises_yes = filtro['Country'].value_counts()

    fig = count_paises_yes.head(5).plot(kind='bar',x='Country', y='Cantidad de personas', title='10 paises con más reportes de problemas de salud mental')

    fig.figure.show()
    
    