import sklearn
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import sys


X, y = load_iris(return_X_y=True)


clf = LogisticRegression(random_state=0, max_iter=1000).fit(X, y)

file_name = 'std1.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(clf, file)
    print(f'Object successfully saved to "{file_name}"')