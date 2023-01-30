import sklearn
import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import sys
import argparse
# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--classifier",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1,  # 0 or more values expected => creates a list
  type=str,
  default=""
)
CLI.add_argument(
  "--data",  # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  action='append',
  type=float,
  default=[]
)
args = CLI.parse_args()
X, y = load_iris(return_X_y=True)

data = [args.data]
file_loc = args.classifier[0]
print(data)
print(file_loc)


with open(file_loc, 'rb') as file:
    clf = pickle.load(file)
    print(f'Object successfully loaded')


print(clf.predict_proba(data))
# Eventually return this value