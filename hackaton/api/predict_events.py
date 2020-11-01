import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


meropr = pd.read_csv('api/events_for_learn.csv', sep='%')
tfidf = TfidfVectorizer(stop_words='english')
meropr['meta'] = meropr['meta'].fillna('')
tfidf_matrix = tfidf.fit_transform(meropr['meta'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)