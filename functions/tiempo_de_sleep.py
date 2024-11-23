import pandas as pd
import matplotlib.pyplot as plt


def nivel_de_estres_tiempo_sueño(dataset:pd.DataFrame) -> tuple:
      
    # Separar el dataset en dos grupos basados en las horas de sueño
    less_than_7 = dataset[dataset['Sleep_Hours'] < 7]  # Personas que duermen menos de 7 horas
    more_than_7 = dataset[dataset['Sleep_Hours'] >= 7]  # Personas que duermen 7 horas o más
    
    # Contar las frecuencias de los niveles de estrés (Stress_Level) para cada grupo
    stress_counts_lt7 = less_than_7['Stress_Level'].value_counts()  # Conteo para menos de 7 horas
    stress_counts_mt7 = more_than_7['Stress_Level'].value_counts()  # Conteo para 7 o más horas

    # Crear gráficos para comparar los niveles de estrés entre los dos grupos
    fig, ax = plt.subplots(1, 2, figsize=(12, 6), sharey=True)  # Dos gráficos lado a lado

    # Gráfico para el grupo con menos de 7 horas de sueño
    stress_counts_lt7.plot(kind='bar', ax=ax[0], color='skyblue', alpha=0.7)
    ax[0].set_title('Niveles de Estrés (< 7 horas de sueño)')  # Título del gráfico
    ax[0].set_xlabel('Nivel de Estrés')  # Etiqueta del eje X
    ax[0].set_ylabel('Cantidad de Personas')  # Etiqueta del eje Y
    ax[0].grid(axis='y', linestyle='--', alpha=0.5)  # Líneas de la cuadrícula para facilitar lectura

    # Gráfico para el grupo con 7 o más horas de sueño
    stress_counts_mt7.plot(kind='bar', ax=ax[1], color='salmon', alpha=0.7)
    ax[1].set_title('Niveles de Estrés (>= 7 horas de sueño)')  # Título del gráfico
    ax[1].set_xlabel('Nivel de Estrés')  # Etiqueta del eje X
    ax[1].grid(axis='y', linestyle='--', alpha=0.5)  # Líneas de la cuadrícula para facilitar lectura

    texto_analisis = 'La gráfica sugiere que dormir 7 o más horas puede estar asociado con menores niveles de estrés bajo, pero no necesariamente reduce los niveles de estrés alto o medio. La calidad del sueño y otros factores de estilo de vida también juegan un papel crucial en los niveles de estrés.'

    fig.savefig('./assets/nivel_de_estres_tiempo_sueño.png')

    return ('./assets/nivel_de_estres_tiempo_sueño.png', texto_analisis )

def salud_mental_tiempo_sueño (dataset:pd.DataFrame) -> tuple:
       # Separar el dataset en dos grupos basados en las horas de sueño
    less_than_7 = dataset[dataset['Sleep_Hours'] < 7]  # Personas que duermen menos de 7 horas
    more_than_7 = dataset[dataset['Sleep_Hours'] >= 7]  # Personas que duermen 7 horas o más
    


    # Contar las frecuencias de las condiciones de salud mental (Mental_Health_Condition) para cada grupo
    mental_health_lt7 = less_than_7['Mental_Health_Condition'].value_counts()  # Menos de 7 horas
    mental_health_mt7 = more_than_7['Mental_Health_Condition'].value_counts()  # 7 o más horas

    # Crear gráficos para comparar las condiciones de salud mental entre los dos grupos
    fig, ax = plt.subplots(1, 2, figsize=(12, 6), sharey=True)  # Dos gráficos lado a lado

    # Gráfico para el grupo con menos de 7 horas de sueño
    mental_health_lt7.plot(kind='bar', ax=ax[0], color='blue', alpha=0.7)
    ax[0].set_title('Salud Mental (< 7 horas de sueño)')  # Título del gráfico
    ax[0].set_xlabel('Condición de Salud Mental')  # Etiqueta del eje X
    ax[0].set_ylabel('Cantidad de Personas')  # Etiqueta del eje Y
    ax[0].grid(axis='y', linestyle='--', alpha=0.5)  # Líneas de la cuadrícula para facilitar lectura

    # Gráfico para el grupo con 7 o más horas de sueño
    mental_health_mt7.plot(kind='bar', ax=ax[1], color='red', alpha=0.7)
    ax[1].set_title('Salud Mental (>= 7 horas de sueño)')  # Título del gráfico
    ax[1].set_xlabel('Condición de Salud Mental')  # Etiqueta del eje X
    ax[1].grid(axis='y', linestyle='--', alpha=0.5)  # Líneas de la cuadrícula para facilitar lectura

    texto_analisis = 'La gráfica muestra que la duración del sueño, ya sea menos de 7 horas o 7 horas o más, no parece ser el único factor determinante en la presencia de problemas de salud mental, ya que ambos grupos presentan cifras similares'

    fig.savefig('./assets/salud_mental_tiempo_sueño.png')

    return('./assets/salud_mental_tiempo_sueño.png', texto_analisis )