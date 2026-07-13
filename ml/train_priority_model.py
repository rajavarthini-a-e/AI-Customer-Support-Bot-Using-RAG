import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("dataset/priority.csv")

X = df["text"].str.lower()
y = df["priority"]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

prediction = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, prediction))

joblib.dump(model, "models/priority_model.pkl")
joblib.dump(vectorizer, "models/priority_vectorizer.pkl")

print("Priority Model Saved!")