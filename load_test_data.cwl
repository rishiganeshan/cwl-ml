# File header
cwlVersion: v1.2
class: CommandLineTool

# Command line tool inputs
inputs:
    data: File
    pyfile: File

# Specifying the program to run
baseCommand: [python3]

arguments: [$(inputs.pyfile), --data, $(inputs.data)]

# Command arguments

# Outputs section
outputs:
  labelled_test_data:
    type: File
    outputBinding:
      glob: labelled_test_data.pkl

# Running in a container
