# import os
# import json
# import requests
# import numpy as np
# import matplotlib.pyplot as plt
# print("Yooooooooooooooooooooo")
# def show(idx, title):
#     plt.figure()
#     plt.imshow(test_images[idx].reshape(28,28))
#     plt.axis('off')
#     plt.title('\n\n{}'.format(title), fontdict={'size': 16})

# # Load test images and labels from NumPy files
# test_images = np.load("test_images.npy")
# test_labels = np.load("test_labels.npy")
# class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

# # Serialize test images to JSON
# data = json.dumps({"signature_name": "serving_default", "instances": test_images[0:3].tolist()})

# # Send a request to the TensorFlow Serving instance
# headers = {"content-type": "application/json"}
# json_response = requests.post('http://localhost:8501/v1/models/fashion_model:predict', data=data, headers=headers)
# predictions = json.loads(json_response.text)['predictions']

# for i in range(0, 3):
#     show(i, 'The model thought this was a {} (class {}), and it was actually a {} (class {})'.format(
#         class_names[np.argmax(predictions[i])], np.argmax(predictions[i]), class_names[test_labels[i]], test_labels[i]))

print("nkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

import json
import requests
import numpy as np
print("nkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")

instances = [[1.0], [2.0], [5.0]]
data = json.dumps({"instances": instances})
print("nkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
headers = {"content-type": "application/json"}
json_response = requests.post(
    "http://localhost:8501/v1/models/regression_experiments:predict",
    data=data,
    headers=headers,
)

predictions = json.loads(json_response.text)["predictions"]

with open("predictions.txt", "w") as f:
    for i, pred in enumerate(predictions):
        f.write(f"Instance {i}: Input = {instances[i]}, Prediction = {pred}\n")
