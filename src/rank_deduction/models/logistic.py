from sklearn.linear_model import LogisticRegression

def get_logistic() :
    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
        random_state=42
    )
    return model