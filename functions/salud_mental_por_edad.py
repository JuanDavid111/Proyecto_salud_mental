import pandas as pd
import matplotlib.pyplot as plt

def salud_mental_edades(dataset: pd.DataFrame) -> tuple:
    mascara1 = ((dataset['Age'] >= 18) & (dataset['Age'] <= 33) & (dataset['Mental_Health_Condition'] == "Yes"))
    primer_rango = dataset[mascara1]  
  
    mascara2 = ((dataset['Age'] >= 34) & (dataset['Age'] <= 49) & (dataset['Mental_Health_Condition'] == "Yes"))
    segundo_rango = dataset[mascara2]  
 
    mascara3 = ((dataset['Age'] >= 50) & (dataset['Age'] <= 65) & (dataset['Mental_Health_Condition'] == "Yes"))
    tercer_rango = dataset[mascara3]  
 
    # se convierte a diccionario para hacer la gráfica
    diccionario_aux = {
        '18-33 años': primer_rango.shape[0],
        '34-39 años': segundo_rango.shape[0],
        '40-65 años': tercer_rango.shape[0]
    }

    # Crear un gráfico de barras
    plt.figure(figsize=(8, 5))
    plt.bar(diccionario_aux.keys(), diccionario_aux.values(), color=['blue', 'orange', 'green'])
    plt.title('Rango de edad con mayor indice de problemas de salud mental')
    plt.xlabel('Rango de Edad')
    plt.ylabel('Número de Personas')
    plt.grid(axis='y')
    
    texto_analisis = "Al analizar y comparar entre tres rango de edades que son los aduntos jóvenes; los adultos de mediana edad y los adultos mayores se puede visualizar que los adultos mayores suelen tener mayores problemas de salud mental y en segundo lugar los adultos jóvenes. El estrés laboral, las responsabilidades familiares, y la planificación financiera pueden ser factores significativos que contribuyen a los problemas de salud mental en los rangos de edad más altos."

    plt.savefig('./assets/salud_mental_edades_grafica.png')


    return ('./assets/salud_mental_edades_grafica.png', texto_analisis)
