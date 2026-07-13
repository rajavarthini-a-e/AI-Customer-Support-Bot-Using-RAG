import joblib

model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/sentiment_vectorizer.pkl")

while True:
    text = input("Enter sentence (exit to quit): ")

    if text.lower() == "exit":
        break

    vector = vectorizer.transform([text.lower()])

    prediction = model.predict(vector)

    print("Sentiment:", prediction[0])