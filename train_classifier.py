import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import argparse
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture


CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--data",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1, 
  type=str,
  default=""
)
args = CLI.parse_args()

file_name = args.data[0]
with open(file_name, 'rb') as file:
    X = pickle.load(file)
    y = pickle.load(file)
    print(X)
    print(y)


clf = LogisticRegression(random_state=0, max_iter=1000).fit(X, y)
# clf = MLPClassifier(random_state=0, max_iter=1000).fit(X, y)
# clf = KNeighborsClassifier().fit(X, y)
# clf = GaussianProcessClassifier(random_state=0).fit(X, y)
# clf = DecisionTreeClassifier().fit(X, y)
# clf = RandomForestClassifier().fit(X, y)
# clf = GaussianNB().fit(X, y)
# clf = GaussianMixture().fit(X)
# clf = KMeans().fit(X)


file_name = 'clf.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(clf, file)
    print(f'Object successfully saved to "{file_name}"')



