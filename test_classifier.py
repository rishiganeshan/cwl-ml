import pickle
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
  nargs="*",
  type=float,
  default=[]
)
args = CLI.parse_args()

data = [args.data]
file_loc = args.classifier[0]
print(data)
print(file_loc)


with open(file_loc, 'rb') as file:
    clf = pickle.load(file)
    print(f'Object successfully loaded')

print(clf.predict(data))
# print(clf.predict_proba(data))
# Eventually return this value