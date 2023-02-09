import pickle
import argparse
import pandas as pd
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
  nargs=1,
  type=str,
  default=""
)
args = CLI.parse_args()

test_data_file = args.classifier[0]
clf_file = args.classifier[0]

test_data = pd.read_csv(test_data_file)


with open(clf_file, 'rb') as file:
    clf = pickle.load(file)

print(clf.predict(test_data))