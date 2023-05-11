import calendar
from fastapi import FastAPI
import pandas as pd

df_expanded_final = pd.read_csv('/Users/melisatirabassi/Library/CloudStorage/OneDrive-Personal/Documentos/Diplomatura Data Science/Henry/dataset_movies_con_ETL.csv')
df_expanded_final['release_date'] = pd.to_datetime(df_expanded_final['release_date'])

app = FastAPI()

@app.get("/")
def read_root():
    return {"Trabajo Final 1 ": "Henry"}

@app.get('/cant_peliculas_mes')
def peliculas_mes(mes:str):
    # creo una columna con el mes
    df_expanded_final['mes'] = df_expanded_final['release_date'].dt.month.map(lambda x: calendar.month_name[x])
    # Obtener la cantidad de películas estrenadas ese mes
    respuesta = len(df_expanded_final[df_expanded_final['mes'] == mes])
    return {'mes': mes, 'cantidad': respuesta}

@app.get('/cant_peliculas_dia')
def peliculas_dia(dia:str):
    # creo una columna con el dia
    df_expanded_final['dia_semana'] = df_expanded_final['release_date'].dt.day_name()
    # Obtener la cantidad de películas estrenadas ese dia de la semana
    respuesta = len(df_expanded_final[df_expanded_final['dia_semana'] == dia])
    return {'dia': dia, 'cantidad': respuesta}

@app.get('/datos_por_franquicia')
def franquicia(franquicia:str):
    # Lógica para obtener la cantidad de películas, ganancia total y promedio de una franquicia
    cantidad = len(df_expanded_final[df_expanded_final['name_belongs_to_collection'] == franquicia])
    # se creo la columna ganacia
    df_expanded_final['ganancia']=df_expanded_final['revenue']-df_expanded_final['budget']
    #se realizan los calculos
    filtered_data = df_expanded_final.loc[df_expanded_final['name_belongs_to_collection'] == franquicia]
    ganancia_total = filtered_data['ganancia'].sum()
    ganancia_promedio =filtered_data['ganancia'].mean()
    return {'franquicia': franquicia, 'cantidad de peliculas': cantidad, 'ganancia_total': ganancia_total, 'ganancia_promedio': ganancia_promedio}

@app.get('/peliculas_por_pais')
def peliculas_pais(pais:str):
    # Lógica para obtener la cantidad de películas producidas en un país
    respuesta = len(df_expanded_final[df_expanded_final['name_production_countries'] == pais])
    return {'pais': pais, 'cantidad': respuesta}

@app.get('/datos_por_productora')
def productoras(productora:str):
    # Lógica para obtener la ganancia total y cantidad de películas de una productora
    filtered_data = df_expanded_final.loc[df_expanded_final['name_production_companies'] == productora]
    ganancia_total = filtered_data['ganancia'].sum()
    cantidad = len(df_expanded_final[df_expanded_final['name_production_companies'] == productora])
    return {'productora': productora, 'ganancia_total': ganancia_total, 'cantidad': cantidad}

@app.get('/datos_por_pelicula')
def retorno(pelicula:str):
    # Lógica para obtener la inversión, ganancia, retorno y año de una película
    inversion = df_expanded_final.loc[df_expanded_final['title'] == pelicula, 'budget'].item()
    # se creo la columna ganacia
    df_expanded_final['ganancia']=df_expanded_final['revenue']-df_expanded_final['budget']
    ganancia = df_expanded_final.loc[df_expanded_final['title'] == pelicula, 'ganancia'].item()
    retorno = df_expanded_final.loc[df_expanded_final['title'] == pelicula, 'return'].item()
    anio = df_expanded_final.loc[df_expanded_final['title'] == pelicula, 'release_year'].item()
    return {'pelicula': pelicula, 'inversion': inversion, 'ganancia': ganancia, 'retorno': retorno, 'anio': anio}
