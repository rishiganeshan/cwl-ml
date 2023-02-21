# File header
cwlVersion: v1.2
class: CommandLineTool

# Command line tool inputs
inputs:
    pyfile: File

# Specifying the program to run
baseCommand: [python3]

arguments: [$(inputs.pyfile)]

# Command arguments

# Outputs section
outputs:
  features:
    type: File
    outputBinding:
      glob: features.pkl
  labels:
    type: File
    outputBinding:
      glob: labels.pkl
  ds_test:
    type: File
    outputBinding:
      glob: ds_test.pkl
  class_names:
    type: File
    outputBinding:
      glob: class_names.pkl
  ds_train_batch:
    type: File
    outputBinding:
      glob: ds_train_batch.pkl
    

# Running in a container
