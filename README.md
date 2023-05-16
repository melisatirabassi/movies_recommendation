# Lab 1 Henry

En el GitHub https://github.com/santivalor van a encontrar dos repositorios publicos https://github.com/santivalor/labs1.git y https://github.com/santivalor/labs1_ML.git. 

En el primero esta el codigo del ETL solicitado sobre el dataset_movies y los archivos para el deploy de FastAPI en Render. En este caso los endpoints de la FAST API son consultas que se realizan sobre el dataset luego de realizar las tranformaciones.

En labs1_ML van a encontrar el codigo completo ETL + Modelo de Machine Learning (ML) y los archivos para el deploy de FastAPI en Render. En este ultimo caso el resultado del endpoint es la recomendacion de 5 peliculas ordenadas por score de similitud una vez que el usuario ingresa una pelicula (lista de 6 peliculas = pelicula ingresada + 5 recomendaciones).
El deploy en Render del modelo de ML no se pudo realizar ya que se esta utilizando la version gratitua de Render y la implemntacion de la API requiere mas de 512 MB. Igualmente, se dejaron los archivos necesarios para el deploy en el repositorio y si se ejeuta el main.py en la maquina la API funciona de forma local.

El codigo en Python fue ejecutado en Google Colab por falta de capacidad en la maquina local. Se esta utilizando la version gratuita de Colab por lo que para realizar el modelo de machine learning se tuvo que filtrar el dataset movies por peliculas realizadas en Estados Unidos asi Colab no colapsaba al realizar el procesamiento de lenguaje natural.


# Tranformaciones

Se cargo el dataset_movies.csv a GoogleColab. Se procedio a realizar un analisis preliminar y se realizaron las siguientes transformaciones solicitadas:
Se desanidaron los campos como belongs_to_collection, production_companies y otros.
Los valores nulos de los campos revenue, budget deben son rellenados por el número 0.
Los valores nulos del campo release date se eliminaron
La columna release_date se cambio a formato fecha AAAA-mm-dd y se creo la columna release_year con el año de la fecha de estreno.
Secreo la columna return dividiendo revenue / budget, cuando no hay datos disponibles para calcularlo se toma el valor 0.
Se eliminaron las columnas que no serán utilizadas, video,imdb_id,adult,original_title,vote_count,poster_path y homepage
Una vez realizadas estas tranformaciones se guardo el nuevo dataset en Dropbox como .csv


#Fastapi

Con el dataset tranformado en Dropbox se creo una API con Fastapi. Con el archivo main.py ubicado en el repositorio labs1 se puede ejecutar la API cuyo endpoints son los siguientes:
def peliculas_mes(mes): '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes (nombre del mes, en str, ejemplo 'enero') historicamente''' return {'mes':mes, 'cantidad':respuesta}
def peliculas_dia(dia): '''Se ingresa el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia (de la semana, en str, ejemplo 'lunes') historicamente''' return {'dia':dia, 'cantidad':respuesta}
def franquicia(franquicia): '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio''' return {'franquicia':franquicia, 'cantidad':respuesta, 'ganancia_total':respuesta, 'ganancia_promedio':respuesta}
def peliculas_pais(pais): '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo''' return {'pais':pais, 'cantidad':respuesta}
def productoras(productora): '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron''' return {'productora':productora, 'ganancia_total':respuesta, 'cantidad':respuesta}
def retorno(pelicula): '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo''' return {'pelicula':pelicula, 'inversion':respuesta, 'ganacia':respuesta,'retorno':respuesta, 'anio':respuesta}


#Render 

En la ubicacion del archivo main.py en la maquina local se creo un archivo Dockerfile (sin extension), un entorno virtual (myenv) donde se instalaron las librerias que utiliza la API (pandas, numpy, requests, uvicorn, Fastapi, joblib, etc) y luego se genero el archivo requirements.txt haciendo freeze de myenv.
Los archivos Dockerfile, main.py y requirements.txt se cargan en el repositorio publico labs1. Se creo un usuario en render.com y se pocedio a crear una Web Service desde el repositorio publico de GitHub (Docker).
https://movie-etl.onrender.com/docs


#Modelo de Machine Learning

Una vez realizadas las transformaciones
