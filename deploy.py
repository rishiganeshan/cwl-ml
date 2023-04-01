import tensorflow as tf
import numpy as np
import os
import csv

def make_predictions(model_path, n_samples=10):
    model = tf.keras.models.load_model(model_path)
    x_random = np.random.uniform(0, 10, n_samples)
    y_pred = model.predict(x_random)
    return x_random, y_pred

def save_predictions_to_csv(file_name, model_name, x_random, y_pred):
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([model_name])
        writer.writerow(["Random input data:"] + list(x_random))
        writer.writerow(["Predicted output data:"] + list(y_pred.squeeze()))
        writer.writerow([])

if __name__ == "__main__":
    import sys
    print("YooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYoooooooo")

    saved_models_dir = sys.argv[1]
    model_paths = [os.path.join(saved_models_dir, model) for model in os.listdir(saved_models_dir) if os.path.isdir(os.path.join(saved_models_dir, model))]
    print(f"Model paths: {model_paths}")
    print("YooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYooooooooYoooooooo")
    for model_path in model_paths:
        model_name = os.path.basename(model_path)
        x_random, y_pred = make_predictions(model_path)
        save_predictions_to_csv("predictions.csv", model_name, x_random, y_pred)
