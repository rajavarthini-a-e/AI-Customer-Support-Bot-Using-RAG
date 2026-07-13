import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("dataset/sentiment.csv")

X = df["text"].str.lower()
y = df["sentiment"]

# TF-IDF
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model = LogisticRegression()

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Save
joblib.dump(model, "models/sentiment_model.pkl")
joblib.dump(vectorizer, "models/sentiment_vectorizer.pkl")

print("Sentiment Model Saved!")