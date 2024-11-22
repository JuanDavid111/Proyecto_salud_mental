import pandas as pd
import matplotlib.pyplot as plt


def top_10_profesiones_peor_salud_mental (dataset: pd.DataFrame) -> tuple :
    """
    Analiza las profesiones con peor salud mental basándose en la columna 'Severity'.
    Genera gráficos generales para las 10 profesiones con más casos de 'High' en 'Severity'.
    También imprime una lista de todas las profesiones en el dataset.

    :param dataset: DataFrame con las columnas necesarias, incluyendo 'Occupation' y 'Severity'.
    """
    # Listar todas las profesiones únicas en el dataset
    all_professions = dataset['Occupation'].unique()
    print(f"Estas son las profesiones en el dataset:\n{', '.join(all_professions)}\n")
    
    # Filtrar datos con 'Severity' == 'High'
    severe_cases = dataset[dataset['Severity'] == 'High']
    
    # Contar el número de casos graves por profesión
    severe_by_profession = severe_cases['Occupation'].value_counts()
    
    # Verificar si hay menos de 10 profesiones con casos graves
    num_professions = min(len(severe_by_profession), 10)
    print(f"Analizando las {num_professions} profesiones con peor salud mental:\n")
    print(severe_by_profession.head(num_professions))

    # Filtrar las 10 peores profesiones (o menos si no hay suficientes)
    worst_professions = severe_by_profession.head(num_professions)
    
    # Crear un gráfico de barras
    plt.figure(figsize=(10, 6))
    worst_professions.plot(kind='bar', color='tomato', alpha=0.8)
    plt.title('10 Profesiones con Peor Salud Mental (Casos de Severidad Alta)')
    plt.xlabel('Profesión')
    plt.ylabel('Cantidad de Casos Graves')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    grafica_top_10 = plt.figure()
    
    return(grafica_top_10, '')


def analisis_por_profesion(dataset: pd.DataFrame, profession ) -> tuple :
    """
    Analiza una profesión específica y, en el mismo proceso, calcula estadísticas
    de todas las profesiones para relacionarlas con la salud mental, nivel de estrés 
    y horas de sueño.

    :param dataset: DataFrame con las columnas necesarias.
    :param profession: Nombre de la profesión a analizar.
    """
    # Calcular estadísticas generales para todas las profesiones
    profession_stats = dataset.groupby('Occupation').agg({
        'Severity': lambda x: (x == 'High').sum(),  # Conteo de casos 'High' en Severity
        'Stress_Level': lambda x: x.value_counts().to_dict(),  # Distribución de Stress_Level
        'Sleep_Hours': 'mean'  # Promedio de horas de sueño
    }).reset_index()

    # Ordenar por cantidad de casos graves ('High')
    profession_stats = profession_stats.rename(columns={'Severity': 'Severe_Count'})
    profession_stats = profession_stats.sort_values(by='Severe_Count', ascending=False)

    # Mostrar resumen general de estadísticas
    # print("Estadísticas generales por profesión:\n")
    # print(profession_stats)
    # print("\n")

    # Verificar si la profesión especificada está en el dataset
    if profession not in profession_stats['Occupation'].values:
        print(f"No se encontraron datos para la profesión: {profession}")
        return

    # Obtener los datos específicos de la profesión
    profession_data = profession_stats[profession_stats['Occupation'] == profession].iloc[0]

    # Extraer valores relevantes
    severe_count = profession_data['Severe_Count']
    avg_sleep = profession_data['Sleep_Hours']
    stress_distribution = profession_data['Stress_Level']

    # Imprimir estadísticas específicas de la profesión
    # print(f"Análisis para la profesión: {profession}\n")
    # print(f"Casos graves ('High') de salud mental: {severe_count}")
    # print(f"Promedio de horas de sueño: {avg_sleep:.2f}")
    # print(f"Distribución de niveles de estrés: {stress_distribution}")

    # Crear gráficos para la profesión específica
    # Gráfico de barras para la distribución de estrés
    plt.figure(figsize=(8, 5))
    pd.Series(stress_distribution).plot(kind='bar', color='skyblue', alpha=0.8)
    plt.title(f'Niveles de Estrés en {profession}')
    plt.xlabel('Nivel de Estrés')
    plt.ylabel('Cantidad de Personas')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    return (plt.figure(), '')