# cwlVersion: v1.0
# class: CommandLineTool

# hints:
#   DockerRequirement:
#     dockerPull: tensorflow/serving

# baseCommand: ["/bin/bash", "-c"]

# arguments:
#   - valueFrom: "tensorflow_model_server --rest_api_port=9001 --model_name=regression_experiments --model_base_path=/myProject/saved_models/regression_experiments"
#     shellQuote: false

# inputs:
#   saved_models:
#     type: Directory
#     inputBinding:
#       prefix: -v
#       separate: false
#       valueFrom: "$(inputs.saved_models.path):/myProject/saved_models"

# outputs:
#   tensorflow_serving_log:
#     type: stdout

# stdout: tensorflow_serving.log


# docker run --rm -it -v /Users/rishiganeshan/Desktop/myProject/saved_models:/myProject/saved_models -p 9001:9001 tensorflow/serving /bin/bash -c "tensorflow_model_server --rest_api_port=9001 --model_name=regression_experiments --model_base_path=/myProject/saved_models/regression_experiments"

# docker run --rm -it -v /Users/rishiganeshan/Desktop/myProject/saved_models:/myProject/saved_models -p 9001:9001 tensorflow/serving /bin/bash -c "tensorflow_model_server --rest_api_port=9001 --model_name=myModel --model_base_path=/myProject/saved_models/1"

# docker run --rm -it -v /Users/rishiganeshan/Desktop/myProject/saved_models/1:/models/myModel -p 9001:9001 tensorflow/serving /bin/bash -c "tensorflow_model_server --rest_api_port=9001 --model_name=myModel --model_base_path=/models"

# docker run -it --entrypoint /bin/bash -v /Users/rishiganeshan/Desktop/myProject/saved_models:/myProject/saved_models -p 9001:9001 tensorflow/serving



# docker run -it -v /Users/rishiganeshan/Desktop/myProject/saved_models:/myProject/saved_models -p 9001:9001 tensorflow/serving /bin/bash -c "tensorflow_model_server --rest_api_port=9001 --model_name=regression_experiments --model_base_path=/myProject/saved_models"

# docker run -it -v /Users/rishiganeshan/Desktop/myProject/saved_models:/myProject/saved_models -p 9001:9001 tensorflow/serving /bin/bash -c "tensorflow_model_server --rest_api_port=9001 --model_name=regression_experiments --model_base_path=/myProject/saved_models"




cwlVersion: v1.2
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: tensorflow/serving
baseCommand: |
  docker run -p 8500:8500 \
             -p 8501:8501 \
             --mount type=bind,source=$(inputs.saved_models.path),target=/models \
             -e MODEL_NAME=1 \
             -e MODEL_BASE_PATH=/models/saved_models/1 \
             -t tensorflow/serving:latest & \
  docker run -p 8502:8500 \
             -p 8503:8501 \
             --mount type=bind,source=$(inputs.saved_models.path),target=/models \
             -e MODEL_NAME=2 \
             -e MODEL_BASE_PATH=/models/saved_models/2 \
             -t tensorflow/serving:latest
inputs:
  saved_models:
    type: Directory
    inputBinding:
      prefix: --mount
      separate: false
      valueFrom: "$(inputs.saved_models.path):/models"
outputs:
  tensorflow_serving_log:
    type: stdout



