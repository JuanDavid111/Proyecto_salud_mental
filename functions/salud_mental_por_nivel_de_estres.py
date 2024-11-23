import pandas as pd
import matplotlib.pyplot as plt


def salud_mental_por_nivel_de_estres(df: pd.DataFrame) -> tuple:
    grouped_data = df.groupby(['Mental_Health_Condition', 'Stress_Level']).size().unstack()

# Mostramos los datos 
    print(grouped_data)

    # Crear el gráfico de barras agrupadas
    grouped_data.plot(kind='bar')

    # Personalizar el gráfico
    plt.title('Comparación de niveles de estrés entre Personas Diagnosticadas')
    plt.xlabel('Condición Diagnosticadas')
    plt.ylabel('Cantidad de Personas')
    plt.legend(title='Nivel de Estrés')
    texto_analisis = "La gráfica sugiere una clara relación entre el nivel de estrés y los problemas de salud mental. Las personas con altos niveles de estrés tienen una mayor probabilidad de ser diagnosticadas con problemas de salud mental, mientras que aquellas con bajos niveles de estrés están menos afectadas" 

    plt.savefig('./assets/salud_mental_por_nivel_de_estres_grafica')

    return ('./assets/salud_mental_por_nivel_de_estres_grafica.png',texto_analisis)