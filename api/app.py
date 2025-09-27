import nltk
import ssl
import os

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Only download nltk data if not already present
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

import string
import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from flask import Flask, request, jsonify
from flask_cors import CORS

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Initialize Flask app
app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Enable CORS for React app

# Load and preprocess the dataset
df = pd.read_csv('spam_ham_dataset.csv')

# Clean the text by removing line breaks
df['text'] = df['text'].apply(lambda x: x.replace('\r\n', ' '))

# Initialize stemmer and stopwords
stemmer = PorterStemmer()
stopwords_set = set(stopwords.words('english'))

# Preprocess text for the dataset
corpus = []
for i in range(len(df)):
    text = df['text'].iloc[i].lower()
    text = text.translate(str.maketrans('', '', string.punctuation)).split()
    text = [stemmer.stem(word) for word in text if word not in stopwords_set]
    text = ' '.join(text)
    corpus.append(text)

# Vectorization and model training
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus).toarray()
y = df['label_num']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = RandomForestClassifier(n_jobs=-1)
clf.fit(X_train, y_train)

# Function to preprocess new email text
def preprocess_email(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation)).split()
    text = [stemmer.stem(word) for word in text if word not in stopwords_set]
    return ' '.join(text)

# API endpoint for email classification
@app.route('/api/classify', methods=['POST'])
def classify_email():
    try:
        data = request.get_json()
        if not data or 'email_text' not in data:
            return jsonify({'error': 'Missing email_text in request'}), 400
        
        email_text = data['email_text']
        if not email_text.strip():
            return jsonify({'error': 'Email text cannot be empty'}), 400
        
        preprocessed_email = preprocess_email(email_text)  # Preprocess it
        email_vector = vectorizer.transform([preprocessed_email]).toarray()  # Vectorize it
        prediction = clf.predict(email_vector)  # Make prediction
        prediction_proba = clf.predict_proba(email_vector)[0]  # Get prediction probabilities

        result = "spam" if prediction[0] == 1 else "ham"
        confidence = float(max(prediction_proba))

        return jsonify({
            'prediction': result,
            'confidence': confidence,
            'email_text': email_text
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Email Spam Detector API is running',
        'endpoints': {
            'classify': 'POST /api/classify',
            'health': 'GET /api/health'
        }
    })

@app.route('/api/info', methods=['GET'])
def model_info():
    return jsonify({
        'model': 'Random Forest Classifier',
        'training_data_size': len(df),
        'features': 'TF-IDF with stemming and stopword removal',
        'classes': ['ham', 'spam']
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
