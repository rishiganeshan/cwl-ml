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
  "--ds_test",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1,
  type=str,
  default=""
)
args = CLI.parse_args()

modelFile = args.model[0]
ds_testFile = args.ds_test[0]

with open(modelFile, 'rb') as file:
    model = pickle.load(file)
with open(ds_testFile, 'rb') as file:
    ds_test = pickle.load(file)


test_accuracy = tf.keras.metrics.Accuracy()
ds_test_batch = ds_test.batch(10)

for (x, y) in ds_test_batch:
  # training=False is needed only if there are layers with different
  # behavior during training versus inference (e.g. Dropout).
  logits = model(x, training=False)
  prediction = tf.math.argmax(logits, axis=1, output_type=tf.int64)
  test_accuracy(prediction, y)

print("Test set accuracy: {:.3%}".format(test_accuracy.result()))

tf.stack([y,prediction],axis=1)
