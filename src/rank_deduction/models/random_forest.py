from sklearn.ensemble import RandomForestClassifier

def get_random_forest() :
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        class_weight="balanced",
        random_state=42
    )
    return model