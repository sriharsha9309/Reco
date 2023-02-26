import streamlit as st
import pickle
import pandas as pd
movies=pickle.load(open('title.pkl', 'rb'))
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
movies['overview'] = movies['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(movies['overview'])
tfidf_matrix.shape
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies.index, index=movies['title_x']).drop_duplicates()
indices
def get_reco(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:16]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title_x'].iloc[movie_indices].values
    #df= pd.DataFrame(a)

def main():
    title= st.text_input("Enter the movie")
    if st.button("Recommendations"):
        df=get_reco(title)
        options= st.container().selectbox("Recommendations are", df)
if __name__ == '__main__':
    main()