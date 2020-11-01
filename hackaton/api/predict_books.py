import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


books = pd.read_csv('api/books.csv', sep='%')
tfidf = TfidfVectorizer(stop_words='english')
books['meta'] = books['meta'].fillna('')
tfidf_matrix = tfidf.fit_transform(books['meta'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)