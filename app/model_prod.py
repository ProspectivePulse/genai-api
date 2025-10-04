import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

def train_and_save():
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = LogisticRegression(max_iter=200)
    clf.fit(X, y)
    joblib.dump(clf, "iris_model.pkl")

def load_model():
    try:
        return joblib.load("iris_model.pkl")
    except:
        train_and_save()
        return joblib.load("iris_model.pkl")

model = load_model()

def predict(features: list):
    X = np.array(features).reshape(1, -1)
    return int(model.predict(X)[0])
