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
  "--features",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1,  # 0 or more values expected => creates a list
  type=str,
  default=""
)
CLI.add_argument(
  "--labels",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1,
  type=str,
  default=""
)
args = CLI.parse_args()

featuresFile = args.features[0]
labelsFile = args.labels[0]

with open(featuresFile, 'rb') as file:
    features = pickle.load(file)
with open(labelsFile, 'rb') as file:
    labels = pickle.load(file)

model = tf.keras.Sequential([
  tf.keras.layers.Dense(10, activation=tf.nn.relu, input_shape=(4,)),  # input shape required
  tf.keras.layers.Dense(10, activation=tf.nn.relu),
  tf.keras.layers.Dense(3)
])

predictions = model(features)
predictions[:5]

tf.nn.softmax(predictions[:5])

print("Prediction: {}".format(tf.math.argmax(predictions, axis=1)))
print("    Labels: {}".format(labels))



file_name = 'model.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(model, file)
    print(f'Object successfully saved to "{file_name}"')