from .logistic import get_logistic
from .svm import get_svm
from .random_forest import get_random_forest
from .xgboost import get_xgboost

MODELS = {
    "Regression logistique": get_logistic(),
    "SVM (linéaire)": get_svm(),
    "Forêt aléatoire": get_random_forest(),
    "XGBoost": get_xgboost(),
}
