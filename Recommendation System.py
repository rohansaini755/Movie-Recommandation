import difflib
import streamlit as st
import pandas as pd
import pickle

data = pd.read_csv('F:\\movie_re\\movies1.csv.xls')
model = pickle.load(open('F:\movie_re\Movie_Recommendation.sav', 'rb'))


def prediction(input_data):
    movie = input_data
    list_of_all_movies = data['original_title'].tolist()
    movie_match = difflib.get_close_matches(movie, list_of_all_movies)

    close_match = movie_match[0]

    index_of_movie = data[data.original_title == close_match]['index'].values[0]
    similarity_score = list(enumerate(model[index_of_movie]))

    sorted_similar_movies = sorted(
        similarity_score, key=lambda x: x[1], reverse=True)

    return sorted_similar_movies


def main():
    st.title("Movies Recommendation System")
    movie = st.text_input('Enter the movie name you like')

    movies_list = []
    if st.button('Recommend'):
        if movie =='':
            st.error("Please Enter The Movie Name")
            return

        if len(movies_list) == 0:
          ans = prediction(movie)
          i = 0
          for movie in ans:
            index = movie[0]
            title_from_index = data[data.index == index]['title'].values[0]
            if(i < 10):
             movies_list.append(title_from_index)
             i += 1

        st.success(movies_list)

    
          

    


if __name__ == '__main__':
    main()
