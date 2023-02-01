import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

X, y = load_iris(return_X_y=True)


# clf = LogisticRegression(random_state=0, max_iter=1000).fit(X, y)
# clf = MLPClassifier(random_state=0, max_iter=1000).fit(X, y)
# clf = KNeighborsClassifier().fit(X, y)
# clf = GaussianProcessClassifier(random_state=0).fit(X, y)
# clf = DecisionTreeClassifier().fit(X, y)
# clf = RandomForestClassifier().fit(X, y)
clf = GaussianNB().fit(X, y)


file_name = 'std1.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(clf, file)
    print(f'Object successfully saved to "{file_name}"')