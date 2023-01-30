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
  clf:
    type: File
    outputBinding:
      glob: std1.pkl

# Running in a container
