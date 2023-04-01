cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "deploy.py"]

requirements:
  DockerRequirement:
    dockerPull: "tensorflow/tensorflow:latest"

inputs:
  saved_models:
    type: Directory
    inputBinding:
      position: 1

outputs:
  predictions:
    type: File
    outputBinding:
      glob: "predictions.txt"
