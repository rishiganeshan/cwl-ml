# File header
cwlVersion: v1.2
class: CommandLineTool

# Command line tool inputs
inputs:
    pyfile: File
    features: File
    labels: File
    model: File
    ds_train_batch: File

# Specifying the program to run
baseCommand: [python3]

arguments: [$(inputs.pyfile), --features, $(inputs.features), 
--labels, $(inputs.labels), --model, $(inputs.model), 
--ds_train_batch, $(inputs.ds_train_batch)]

# Command arguments

# Outputs section
outputs:
  model:
    type: File
    outputBinding:
      glob: model.pkl
    

# Running in a container
