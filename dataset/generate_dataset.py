import pandas as pd
import random

order_tracking = [
    "Where is my order?",
    "Track my package",
    "Where is my shipment?",
    "Has my order been shipped?",
    "Delivery status",
    "My parcel is delayed",
    "When will my package arrive?",
    "Track my delivery",
    "Order not delivered",
    "Locate my package"
]

refund = [
    "I want a refund",
    "Refund my payment",
    "Return this product",
    "Money back",
    "Issue a refund",
    "I need reimbursement",
    "Refund request",
    "Product is damaged",
    "Return and refund",
    "Refund for my order"
]

payment = [
    "Payment failed",
    "Money deducted",
    "Transaction failed",
    "Payment pending",
    "Double payment",
    "Unable to pay",
    "Card payment failed",
    "UPI payment failed",
    "Payment unsuccessful",
    "Charged twice"
]

cancellation = [
    "Cancel my order",
    "I want to cancel",
    "Cancel purchase",
    "Stop my order",
    "Cancel before shipping",
    "Order cancellation",
    "I don't need this anymore",
    "Please cancel",
    "Cancel immediately",
    "Withdraw my order"
]

data = []

for _ in range(125):
    data.append([random.choice(order_tracking), "Order Tracking"])
    data.append([random.choice(refund), "Refund"])
    data.append([random.choice(payment), "Payment Issue"])
    data.append([random.choice(cancellation), "Cancellation"])

df = pd.DataFrame(data, columns=["text", "intent"])

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv("dataset/intents.csv", index=False)

print("Dataset Created Successfully!")
print(df.head())