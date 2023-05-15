from fastapi import FastAPI
import pandas as pd
import numpy as np
import joblib
import requests
import io


#df_preliminar = pd.read_csv('/Users/melisatirabassi/Library/CloudStorage/OneDrive-Personal/Documentos/Diplomatura Data Science/Henry/dataset_ml.csv')
#similarity_matrix = joblib.load('modelo.joblib')

def download_file_from_dropbox(access_token, file_path):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Dropbox-API-Arg": f'{{"path": "{file_path}"}}'
    }
    try:
        response = requests.post(
            "https://content.dropboxapi.com/2/files/download",
            headers=headers
        )
        response.raise_for_status()
        file_data = response.content
        return file_data
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file from Dropbox: {e}")


# Ejemplo de uso
access_token = "sl.BeeEHOvBxH5lkdaadqOknjizUYBAuOYxJUgqqG5WKWSujcBd6jLSzJztT4eNdSUEt7SLKLkhS7_4tnaKxU-kw9jxP_qMqNp7USSvGtacpgXHP2HxB4tsAS5znDJBxyKI28nYStux"
file_path = "/dataset_ml.csv"  # Ruta del archivo en Dropbox
file_path_model = "/modelo.joblib"  # Ruta del archivo en Dropbox
file_data_df = download_file_from_dropbox(access_token, file_path)
file_data_model = download_file_from_dropbox(access_token, file_path_model)
# Procesa el archivo de datos según tus necesidades

df_preliminar= pd.read_csv(io.BytesIO(file_data_df))
similarity_matrix = joblib.load(io.BytesIO(file_data_model))

app = FastAPI()

@app.post("/peliculas_recomendadas")
def predict(data: str):
    # Make predictions using the loaded model
    input_movie_index = df_preliminar.index[df_preliminar['title']==data]
    movie_scores = similarity_matrix[input_movie_index]
    similar_movie_indices = np.argsort(movie_scores)
    similar_movie_indices = similar_movie_indices[-1][::-1]
    similar_movie_indices = similar_movie_indices[:6]
    recommended_movies = []
    for index in similar_movie_indices:
        if index < len(df_preliminar):
            recommended_movies.append(df_preliminar.iloc[index]['title'])
    # Return the predictions as the API response
    return {"predictions": recommended_movies}

