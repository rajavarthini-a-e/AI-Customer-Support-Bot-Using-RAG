from predict import predict_intent

while True:

    query = input("Enter Query (exit to quit): ")

    if query.lower() == "exit":
        break

    intent = predict_intent(query)

    print("Predicted Intent:", intent)