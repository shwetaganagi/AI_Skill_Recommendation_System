import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier


def get_data():
    df = pd.read_csv("data/raw/career_dataset.csv")

    X = df.drop("career", axis=1)
    y = df["career"]

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_encoded,
        test_size=0.2,
        random_state=42,
        stratify=y_encoded
    )

    return X_train, X_test, y_train, y_test, label_encoder


def get_preprocessor():
    return ColumnTransformer(
        transformers=[
            ("skills_tfidf", TfidfVectorizer(), "skills"),
            ("education_ohe", OneHotEncoder(handle_unknown="ignore"), ["education"]),
            ("interests_tfidf", TfidfVectorizer(), "interests"),
            ("experience_num", "passthrough", ["experience"])
        ]
    )


def train_and_save(model, model_name):
    X_train, X_test, y_train, y_test, label_encoder = get_data()

    pipeline = Pipeline([
        ("preprocessing", get_preprocessor()),
        ("classifier", model)
    ])

    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, f"models/{model_name}.pkl")
    joblib.dump(label_encoder, "models/label_encoder.pkl")

    print(f"{model_name} trained successfully")


if __name__ == "__main__":
    models = {
        "logistic_model": LogisticRegression(max_iter=2000),
        "random_forest_model": RandomForestClassifier(n_estimators=200),
        "svm_model": SVC(probability=True),
        "neural_network_model": MLPClassifier(
            hidden_layer_sizes=(128, 64),
            max_iter=500
        )
    }

    for name, model in models.items():
        train_and_save(model, name)