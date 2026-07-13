import joblib

# Load Saved Models
model = joblib.load("models/intent_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


def predict_intent(query):
    query_vector = vectorizer.transform([query])
    prediction = model.predict(query_vector)[0]
    return prediction