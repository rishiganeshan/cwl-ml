import pickle
import argparse
import pandas as pd
# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--data",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1, 
  type=str,
  default=""
)
args = CLI.parse_args()

data_file = args.data[0]


df = pd.read_csv(data_file)

file_name = 'labelled_test_data.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(df, file)
    print(f'Object successfully saved to "{file_name}"')


# print(clf.predict_proba(data))
# Eventually return this value