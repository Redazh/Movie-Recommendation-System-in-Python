import streamlit as st
import pickle
import requests


movies_data = pickle.load(open("movies_data.pkl", 'rb'))
movies_title = movies_data['title'].values
similarity = pickle.load(open("similarity.pkl", 'rb'))

st.header("Movie Recommendation System in Python")

selectvalue=st.selectbox("Select movie from dropdown", movies_title)



def get_picture(id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(id)
     data=requests.get(url).json()
     path = "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
     return path

def movie_recommandation(movies_title,num_of_movies=3):
    index=movies_data[movies_data['title']==movies_title].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommendation=[]
    pictures=[]
    for i in distance[1:num_of_movies+1]:
        recommendation.append(movies_data.iloc[i[0]].title)
        pictures.append(get_picture(movies_data.iloc[i[0]].id))
    return recommendation,pictures




if st.button("Show Result"):
    recommendation,images = movie_recommandation(selectvalue)
    col1,col2,col3=st.columns(3)
    with col1:
        st.text(recommendation[0])
        st.image(images[0])
    with col2:
        st.text(recommendation[1])
        st.image(images[1])
    with col3:
        st.text(recommendation[2])
        st.image(images[2])
   