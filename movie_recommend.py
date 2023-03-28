# Importing Libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

data = pd.read_csv('F:\movie_re\movies1.csv.xls')
# print(data.shape)
# print(data.head())

selected_features = ['genres','keywords', 'tagline', 'cast', 'director']
# print(selected_features)

for feature in selected_features:
    data[feature] = data[feature].fillna('')

combined_features = data['genres']+' '+data['keywords']+' '+data['tagline']+' '+data['cast']+' '+data['director']
# print(combined_features.head())

vectorizer = TfidfVectorizer()
feature_vector = vectorizer.fit_transform(combined_features)

# print(feature_vector[5])

similarity = cosine_similarity(feature_vector)

# print(similarity)

filename = 'Movie_Recommendation.sav'
pickle.dump(similarity,open(filename,'wb'))