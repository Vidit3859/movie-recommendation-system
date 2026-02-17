# 🎬 Movie Recommendation System

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20App-red?logo=streamlit)](https://vidit-ml-movie-recommendation-system.streamlit.app)

A machine learning project that recommends movies based on user preferences using **collaborative filtering** and **content-based filtering**.

This project uses the **MovieLens dataset** and provides a simple **Streamlit web interface** for generating movie recommendations.

---

## Project Overview

Recommendation systems are widely used in platforms like Netflix, Amazon, and Spotify.  
This project demonstrates how to build a basic recommendation engine using:

- User rating similarity (Collaborative Filtering)
- Movie genre similarity (Content-Based Filtering)

The application allows users to select a movie and receive **Top-5 recommendations**.

---

## Dataset

This project uses the **MovieLens Small Dataset**.

Files used:
- `movies.csv`
- `ratings.csv`
- `links.csv`
- `tags.csv`

Dataset source:
https://grouplens.org/datasets/movielens/

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

---

## Machine Learning Approach

### Collaborative Filtering
- Create user-movie rating matrix
- Replace missing values with 0
- Compute cosine similarity between movies
- Recommend similar movies based on rating patterns

### Content-Based Filtering
- Use movie genres as features
- Convert genres using TF-IDF vectorization
- Compute cosine similarity between movies
- Recommend movies with similar genres

---

## Project Structure

```
movie-recommendation-system/
│
├── data/
│   ├── movies.csv
│   ├── ratings.csv
│   ├── links.csv
│   └── tags.csv
│
├── notebook.ipynb
├── recommender.py
├── app.py
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run Streamlit app

```bash
streamlit run app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## Features

- Movie recommendation using collaborative filtering
- Genre-based recommendation system
- Interactive Streamlit UI
- Top-5 movie recommendations
- MovieLens dataset integration

---

## Example Output

Selecting Toy Story (1995) returns recommendations like:

- Toy Story 2 (1999)
- Jurassic Park (1993)
- Independence Day (1996)
- Star Wars (1977)
- Forrest Gump (1994)

---

## Learning Outcomes

From this project, I learned:

- How recommendation systems work
- Collaborative vs content-based filtering
- Cosine similarity in ML
- TF-IDF feature extraction
- Building ML apps using Streamlit
- Structuring ML projects for GitHub

---

## Future Improvements

- Add fuzzy search for movie titles
- Add poster images using TMDB API
- Add hybrid recommendation system
- Deploy the app online
- Add sentiment-based filtering

---