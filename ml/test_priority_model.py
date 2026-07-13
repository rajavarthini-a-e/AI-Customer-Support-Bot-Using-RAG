import joblib

model = joblib.load("models/priority_model.pkl")
vectorizer = joblib.load("models/priority_vectorizer.pkl")

while True:
    query = input("Enter Query (exit to quit): ")

    if query.lower() == "exit":
        break

    vector = vectorizer.transform([query.lower()])

    prediction = model.predict(vector)

    print("Priority:", prediction[0])