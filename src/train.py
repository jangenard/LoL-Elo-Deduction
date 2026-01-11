import os

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import StratifiedKFold, cross_validate, learning_curve
from sklearn.pipeline import Pipeline

from rank_deduction.data.dataset import ScoreboardDataset
from rank_deduction.data.create_csv import create_csv
from rank_deduction.data.get_data import get_data

from rank_deduction.models import MODELS

FEATURES = [
        "total_kills_per_min",
        "kills_per_min",
        "deaths_per_min",
        "kda_ratio",
        "kill_participation",
        "cs_per_min",
        "time"
    ]

def make_pipeline(model):
    return Pipeline([
        ("scaler", StandardScaler()),
        ("clf", model)
    ])

def get_cv():
    cv = StratifiedKFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )
    return cv

def main():
    if not os.listdir("outputs") :
        print("stats.csv doesn't exist")
        path = "data"
        dataset = get_data(path)
        create_csv(dataset)

    df = pd.read_csv("outputs/stats.csv")

    X = df[FEATURES]
    y = df["rank"]

    le = LabelEncoder()
    y_enc = le.fit_transform(y)

    cv = get_cv()

    scoring = {
        "accuracy": "accuracy",
        "f1_macro": "f1_macro"
    }

    results = []

    for name, model in MODELS.items():
        pipe = make_pipeline(model)

        scores = cross_validate(
            pipe,
            X,
            y_enc,
            cv=cv,
            scoring=scoring,
            return_train_score=False
        )

        results.append({
            "Model": name,
            "Accuracy (mean)": scores["test_accuracy"].mean(),
            "F1 Macro (mean)": scores["test_f1_macro"].mean(),
            "Accuracy (std)": scores["test_accuracy"].std(),
            "F1 Macro (std)": scores["test_f1_macro"].std()
        })

    results_df = pd.DataFrame(results).sort_values(
        by="F1 Macro (mean)",
        ascending=False
    )

    print(results_df)

    best_model_name = results_df.iloc[0]["Model"]
    best_model = make_pipeline(MODELS[best_model_name])
    best_model.fit(X, y_enc)

    print(f"\nBest model: {best_model_name}")

    
if __name__ == "__main__" :
    main()