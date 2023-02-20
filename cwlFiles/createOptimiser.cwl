# File header
cwlVersion: v1.2
class: CommandLineTool

# Command line tool inputs
inputs:
    pyfile: File
    features: File
    labels: File
    model: File

# Specifying the program to run
baseCommand: [python3]

arguments: [$(inputs.pyfile), --features, $(inputs.features), 
--labels, $(inputs.labels), --model, $(inputs.model)]

# Command arguments

# Outputs section
outputs:
  model:
    type: File
    outputBinding:
      glob: model.pkl
    

# Running in a container
