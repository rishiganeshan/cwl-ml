cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python"]

requirements:
  DockerRequirement:
    dockerPull: "tensorflow/tensorflow:latest"

inputs:
  train_script:
    type: File
    inputBinding:
      position: 1

outputs:
  saved_models:
    type: Directory
    outputBinding:
      glob: "saved_models"

stdout: train.log
