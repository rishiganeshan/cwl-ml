import os
import sys
from subprocess import Popen
import json
import requests
import numpy as np

# Might need to get rid of the 1
print("yooooooo")
MODEL_DIR = "/saved_models"

os.environ["MODEL_DIR"] = MODEL_DIR

print("yooooooo")

process = Popen([
    "tensorflow_model_server",
    "--rest_api_port=8501",
    "--model_name=regression_experiments",
    "--model_base_path={}".format(MODEL_DIR),
])
print("asdkjasdhkjabfkjsdhfkjsdhfkjsdhfkjshfkdsh")
sys.stdout.flush()
process.wait()
print("asdkjasdhkjabfkjsdhfkjsdhfkjsdhfkjshfkdsh")



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


