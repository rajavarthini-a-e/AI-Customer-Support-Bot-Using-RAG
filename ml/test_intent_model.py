import joblib

# Load model and vectorizer
model = joblib.load("models/intent_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

while True:
    user_input = input("Enter your query (type 'exit' to quit): ")

    if user_input.lower() in ["exit", "quit"]:
        break

    vector = vectorizer.transform([user_input.lower()])

    prediction = model.predict(vector)

    print("Predicted Intent:", prediction[0])