import os
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import pickle
import numpy as np

print("TensorFlow version: {}".format(tf.__version__))
print("TensorFlow Datasets version: ",tfds.__version__)

# Import data
tf.compat.v1.enable_eager_execution()

ds_preview, info = tfds.load('penguins/simple', split='train', with_info=True)
df = tfds.as_dataframe(ds_preview.take(5), info)
print(df)
print(info.features)

class_names = ['Adélie', 'Chinstrap', 'Gentoo']

ds_split, info = tfds.load("penguins/processed", split=['train[:20%]', 'train[20%:]'], as_supervised=True, with_info=True)

ds_test = ds_split[0]
ds_train = ds_split[1]
assert isinstance(ds_test, tf.data.Dataset)

print(info.features)
np_test = np.vstack(tfds.as_numpy(ds_test))
df_test = tfds.as_dataframe(ds_test.take(5), info)
print("Test dataset sample: ")
print(df_test)

df_train = tfds.as_dataframe(ds_train.take(5), info)
print("Train dataset sample: ")
print(df_train)

ds_train_batch = ds_train.batch(32)
tfds.as_numpy(ds_train_batch)
# Hstack vstack dstack hmmmm
np_train_batch = np.dstack(tfds.as_numpy(ds_train_batch))

features, labels = next(iter(ds_train_batch))

print(features)
print(labels)

plt.scatter(features[:,0],
            features[:,2],
            c=labels,
            cmap='viridis')

plt.xlabel("Body Mass")
plt.ylabel("Culmen Length")
# plt.show()


file_name = 'features.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(features, file)
    print(f'Object successfully saved to "{file_name}"')

file_name = 'labels.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(labels, file)
    print(f'Object successfully saved to "{file_name}"')

file_name = 'np_test.pkl'
print(type(np_test))
with open(file_name, 'wb') as file:
    pickle.dump(np_test, file)
    print(f'Object successfully saved to "{file_name}"')

file_name = 'np_train_batch.pkl'
print(type(np_test))
with open(file_name, 'wb') as file:
    pickle.dump(np_train_batch, file)
    print(f'Object successfully saved to "{file_name}"')

file_name = 'class_names.pkl'
with open(file_name, 'wb') as file:
    pickle.dump(class_names, file)
    print(f'Object successfully saved to "{file_name}"')




