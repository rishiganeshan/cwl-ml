import sklearn
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import sys

X, y = load_iris(return_X_y=True)


file_name = 'std1.pkl'
file_loc = '/Users/rishiganeshan/Desktop/CWL/std1.pkl'
with open(file_loc, 'rb') as file:
    clf = pickle.load(file)
    print(f'Object successfully loaded')

clf.predict(X[:2, :])
clf.predict_proba(X[:2, :])
print(clf.score(X, y))