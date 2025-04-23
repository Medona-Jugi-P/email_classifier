import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

def train_model(csv_path='data/combined_emails_with_natural_pii.csv'):
    df = pd.read_csv(csv_path)
    X = df['email']
    y = df['type']

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer(stop_words='english')),
        ('clf', MultinomialNB())
    ])
    pipeline.fit(X, y)

    joblib.dump(pipeline, 'model/classifier.pkl')
    print("Model trained and saved!")
