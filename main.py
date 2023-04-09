import streamlit as st
import pickle
import pandas as pd
import requests

def poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=5420d86058545b790f7d3e55116e81c2&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x : x[1])[1:11]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity=pickle.load(open('similarity.pkl', 'rb'))
st.title('MovieMatch: A Content-Based Movie Recommender System')
movies = pd.DataFrame(movies_dict)
selected_movie_name = st.selectbox('What to watch if you liked this ?', movies['title'].values)
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    row1_col1, row1_col2, row1_col3 = st.columns(3)
    row2_col1, row2_col2, row2_col3 = st.columns(3)
    row3_col1, row3_col2, row3_col3 = st.columns(3)

    with row1_col1:
        st.text(names[0])
        st.image(posters[0])

    with row1_col2:
        st.text(names[1])
        st.image(posters[1])

    with row1_col3:
        st.text(names[2])
        st.image(posters[2])

    with row2_col1:
        st.text(names[3])
        st.image(posters[3])

    with row2_col2:
        st.text(names[4])
        st.image(posters[4])

    with row2_col3:
        st.text(names[5])
        st.image(posters[5])

    with row3_col1:
        st.text(names[6])
        st.image(posters[6])

    with row3_col2:
        st.text(names[7])
        st.image(posters[7])

    with row3_col3:
        st.text(names[8])
        st.image(posters[8])


