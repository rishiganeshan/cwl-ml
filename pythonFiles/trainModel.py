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
CLI.add_argument(
  "--model",  # name on the CLI - drop the `--` for positional/required parameters
  nargs=1,
  type=str,
  default=""
)

args = CLI.parse_args()

featuresFile = args.features[0]
labelsFile = args.labels[0]
modelFile = args.model[0]

with open(featuresFile, 'rb') as file:
    features = pickle.load(file)
with open(labelsFile, 'rb') as file:
    labels = pickle.load(file)
with open(modelFile, 'rb') as file:
    model = pickle.load(file)


loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

def loss(model, x, y, training):
  # training=training is needed only if there are layers with different
  # behavior during training versus inference (e.g. Dropout).
  y_ = model(x, training=training)

  return loss_object(y_true=y, y_pred=y_)

l = loss(model, features, labels, training=False)
print("Loss test: {}".format(l))

# def grad(model, inputs, targets):
#   with tf.GradientTape() as tape:
#     loss_value = loss(model, inputs, targets, training=True)
#   return loss_value, tape.gradient(loss_value, model.trainable_variables)


file_name = 'model.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(model, file)
    print(f'Object successfully saved to "{file_name}"')