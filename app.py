import streamlit as st
from recommender import recommend_movies, recommend_by_genre
import pandas as pd

st.title("🎬 Movie Recommendation System")

movies = pd.read_csv("data/movies.csv")
movie_list = movies["title"].values

movie_selected = st.selectbox("Select a movie", movie_list)

recommendation_type = st.radio(
    "Recommendation type",
    ["Collaborative Filtering", "Content-Based (Genres)"]
)

if st.button("Recommend"):
    
    if recommendation_type == "Collaborative Filtering":
        recommendations = recommend_movies(movie_selected)
    else:
        recommendations = recommend_by_genre(movie_selected)

    st.subheader("Top Recommendations:")
    
    for movie in recommendations:
        st.write(movie)