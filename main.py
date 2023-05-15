from fastapi import FastAPI
import pandas as pd
import numpy as np
import joblib

df_preliminar = pd.read_csv('/Users/melisatirabassi/Library/CloudStorage/OneDrive-Personal/Documentos/Diplomatura Data Science/Henry/dataset_ml.csv')
similarity_matrix = joblib.load('modelo.joblib')

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

