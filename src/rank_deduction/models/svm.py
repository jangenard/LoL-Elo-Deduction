from sklearn.svm import SVC

def get_svm() :
    model = SVC(
        kernel="linear",
        class_weight="balanced",
        probability=True,
        random_state=42
    )
    return model