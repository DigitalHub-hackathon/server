import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


students = pd.read_csv('api/studients_for_learn.csv', sep='%')
tfidf = TfidfVectorizer(stop_words='english')
students['meta'] = students['meta'].fillna('')
tfidf_matrix = tfidf.fit_transform(students['meta'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)