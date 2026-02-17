import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Merge
data = pd.merge(ratings, movies, on="movieId")

# Collaborative filtering matrix
movie_matrix = data.pivot_table(
    index="userId",
    columns="title",
    values="rating"
)

movie_matrix_filled = movie_matrix.fillna(0)

movie_similarity = cosine_similarity(movie_matrix_filled.T)

movie_similarity_df = pd.DataFrame(
    movie_similarity,
    index=movie_matrix_filled.columns,
    columns=movie_matrix_filled.columns
)

# Content-based filtering
movies["genres"] = movies["genres"].str.replace("|", " ")
tfidf = TfidfVectorizer(stop_words="english")
genre_matrix = tfidf.fit_transform(movies["genres"])

genre_similarity = cosine_similarity(genre_matrix, genre_matrix)

genre_similarity_df = pd.DataFrame(
    genre_similarity,
    index=movies["title"],
    columns=movies["title"]
)

def recommend_movies(movie_title, num_recommendations=5):
    if movie_title not in movie_similarity_df.index:
        return []
    scores = movie_similarity_df[movie_title].sort_values(ascending=False)
    return list(scores.iloc[1:num_recommendations+1].index)

def recommend_by_genre(movie_title, num_recommendations=5):
    if movie_title not in genre_similarity_df.index:
        return []
    scores = genre_similarity_df[movie_title].sort_values(ascending=False)
    return list(scores.iloc[1:num_recommendations+1].index)