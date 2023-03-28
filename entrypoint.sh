#!/bin/bash

# Start TensorFlow Serving
/usr/bin/tensorflow_model_server \
  --rest_api_port=9001 \
  --model_name=regression_experiments \
  --model_base_path=/myProject/saved_models &

# Run your additional command here
# For example, a sleep command to keep the container running
sleep infinity
