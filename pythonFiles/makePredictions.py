import os
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import pickle
import argparse
# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--model",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1,
  type=str,
  default=""
)
CLI.add_argument(
  "--class_names",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1,
  type=str,
  default=""
)
args = CLI.parse_args()

modelFile = args.model[0]
class_namesFile = args.class_names[0]

with open(modelFile, 'rb') as file:
    model = pickle.load(file)
with open(class_namesFile, 'rb') as file:
    class_names = pickle.load(file)

predict_dataset = tf.convert_to_tensor([
    [0.3, 0.8, 0.4, 0.5,],
    [0.4, 0.1, 0.8, 0.5,],
    [0.7, 0.9, 0.8, 0.4]
])

# training=False is needed only if there are layers with different
# behavior during training versus inference (e.g. Dropout).
predictions = model(predict_dataset, training=False)

for i, logits in enumerate(predictions):
  class_idx = tf.math.argmax(logits).numpy()
  p = tf.nn.softmax(logits)[class_idx]
  name = class_names[class_idx]
  print("Example {} prediction: {} ({:4.1f}%)".format(i, name, 100*p))