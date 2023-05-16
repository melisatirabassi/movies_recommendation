# Lab 1 Henry

En el GitHub https://github.com/santivalor van a encontrar dos repositorios publicos https://github.com/santivalor/labs1.git y https://github.com/santivalor/labs1_ML.git. 
En el primero esta el codigo del ETL solicitado sobre el dataset_movies y los archivos para el deploy de FastAPI en Render. En este caso los endpoints de la FAST API son consultas que se realizan sobre el dataset luego de realizar el ETL.
En labs1_ML van a encontrar el codigo completo ETL + Modelo de Machine Learning (ML) y los archivos para el deploy de FastAPI en Render. En este ultimo caso el resultado del endpoint es la recomendacion de 5 peliculas ordenadas por score de similitud una vez que el usuario ingresa una pelicula (lista de 6 peliculas = pelicula ingresada + 5 recomendaciones).
El deploy en Render del modelo de ML no se pudo realizar ya que se esta utilizando la version gratitua, la implemntacion de la API requiere mas de 512 MB. Igualmente, se dejaron los archivos necesarios para el deploy en el repositorio y si se ejeuta el main.py en la maquina la API funciona.
