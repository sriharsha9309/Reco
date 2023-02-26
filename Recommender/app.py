import streamlit as st
import pickle
import pandas as pd
import numpy as np
st.title("Movie Recommendation System")
movie_df=pickle.load(open('sriharsha9309/Reco/Recommender/reco.pkl', 'rb'))
a=set(movie_df['title'])
movies=pd.DataFrame(a)
def reco(name):
    matching_movies = [title for title in movie_df['genres'] == name]
    a = movie_df[matching_movies].sort_values('wr', ascending=False).head(11)
    return a['title']
def main():
    genre= st.text_input("Enter the genre")
    if st.button("Recommendations"):
        df=list(reco(genre))
        options=st.container().selectbox("Recommendations are", df)
if __name__ == '__main__':
    main()


