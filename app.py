import streamlit as st
import pickle
import requests
import pandas as pd

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path
feedback_df = pd.DataFrame(columns=["Title", "Feedback"])
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
top_movies_list = pickle.load(open("top_movies_list.pkl", 'rb'))
movies_list=movies['title'].values

st.header("Movie Recommender System")

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")


imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)
selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

def recommend_movies_by_titles(movie_titles):
    movie_poster = []
    movie_title = []
    for title in movie_titles:
        # Find the movie ID using the title (assuming 'movies' DataFrame has 'id' and 'title' columns)
        movie_id = movies[movies['title'] == title]['id'].values
        if len(movie_id) == 0:
            movie_id = None  # Movie not found
        else:
            movie_id = movie_id[0]

        # Fetch the movie poster using 'fetch_poster' function (replace with your actual implementation)
        movie_poster.append(fetch_poster(movie_id))
        movie_title.append(title)

    return movie_title,movie_poster


if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])

    st.write("")
st.write("Recommend movies according to watch history:")
st.write("")
movie_name1, movie_poster1 = recommend_movies_by_titles(top_movies_list)
col1,col2,col3,col4,col5=st.columns(5)
with col1:
    st.text(movie_name1[0])
    st.image(movie_poster1[0])
    user_feedback = st.text_input(f"Enter your feedback:", key=f"feedback_{0}")
    if st.button("Submit", key=f"feedback_button_{0}"):
        feedback_df = pd.concat([feedback_df, pd.DataFrame({"Title": [movie_name1[0]], "Feedback": user_feedback})])
        feedback_df.to_csv("feedback.csv")
        st.success("Feedback saved!")

with col2:
    st.text(movie_name1[1])
    st.image(movie_poster1[1])
    user_feedback1 = st.text_input(f"Enter your feedback:", key=f"feedback_{1}")
    if st.button("Submit", key=f"feedback_button_{1}"):
        feedback_df = pd.concat([feedback_df, pd.DataFrame({"Title": [movie_name1[1]], "Feedback": user_feedback1})])
        feedback_df.to_csv("feedback.csv")
        st.success("Feedback saved!")
with col3:
    st.text(movie_name1[2])
    st.image(movie_poster1[2])
    user_feedback2 = st.text_input("Enter your feedback:", key=f"feedback_{2}")
    if st.button("Submit", key=f"feedback_button_{2}"):
        feedback_df = pd.concat([feedback_df, pd.DataFrame({"Title": [movie_name1[2]], "Feedback": user_feedback2})])
        feedback_df.to_csv("feedback.csv")
        st.success("Feedback saved!")
with col4:
    st.text(movie_name1[3])
    st.image(movie_poster1[3])
    user_feedback3= st.text_input("Enter your feedback:", key=f"feedback_{3}")
    if st.button("Submit", key=f"feedback_button_{3}"):
        feedback_df = pd.concat([feedback_df, pd.DataFrame({"Title": [movie_name1[3]], "Feedback": user_feedback3})])
        feedback_df.to_csv("feedback.csv")
        st.success("Feedback saved!")
with col5:
    st.text(movie_name1[4])
    st.image(movie_poster1[4])
    user_feedback4 = st.text_input("Enter your feedback:", key=f"feedback_{4}")
    if st.button("Submit", key=f"feedback_button_{4}"):
        feedback_df = pd.concat([feedback_df, pd.DataFrame({"Title": [movie_name1[4]], "Feedback": user_feedback4})])
        feedback_df.to_csv("feedback.csv")
        st.success("Feedback saved!")