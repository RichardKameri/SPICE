import pickle
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Load your dataset (ensure it has 'text' and 'label' columns)
df = pd.read_csv('/content/data/reviews_cleaned.csv')

# Feature Extraction
X = df['text']
y = df['label']  # Labels: -1 (Negative), 0 (Neutral), 1 (Positive)

# Convert text into numerical features using TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = vectorizer.fit_transform(X)

# Apply SMOTE for class balancing
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_tfidf, y)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Train a classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Evaluate Model
y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred))

# Save the model and vectorizer
with open('sentiment_model.pkl', 'wb') as model_file:
    pickle.dump(Pipeline([('vectorizer', vectorizer), ('classifier', classifier)]), model_file)
