import pandas as pd
import joblib

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder


def evaluate_model(model_path, model_name):
    df = pd.read_csv("data/raw/career_dataset.csv")

    X = df.drop("career", axis=1)
    y = df["career"]

    encoder = joblib.load("models/label_encoder.pkl")
    y_encoded = encoder.transform(y)

    model = joblib.load(model_path)

    predictions = model.predict(X)

    accuracy = accuracy_score(y_encoded, predictions)
    precision = precision_score(y_encoded, predictions, average="weighted")
    recall = recall_score(y_encoded, predictions, average="weighted")
    f1 = f1_score(y_encoded, predictions, average="weighted")

    return {
        "Model": model_name,
        "Accuracy": round(accuracy, 4),
        "Precision": round(precision, 4),
        "Recall": round(recall, 4),
        "F1 Score": round(f1, 4)
    }


if __name__ == "__main__":
    models = [
        ("models/logistic_model.pkl", "Logistic Regression"),
        ("models/random_forest_model.pkl", "Random Forest"),
        ("models/svm_model.pkl", "SVM"),
        ("models/neural_network_model.pkl", "Neural Network")
    ]

    results = []

    for model_path, model_name in models:
        result = evaluate_model(model_path, model_name)
        results.append(result)

    results_df = pd.DataFrame(results)

    print(results_df)