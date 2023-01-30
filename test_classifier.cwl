# File header
cwlVersion: v1.2
class: CommandLineTool

# Command line tool inputs
inputs:
    pyfile: File
    X: float[]
    clf: File

# Specifying the program to run
baseCommand: [python3]

arguments: [$(inputs.pyfile), --classifier, $(inputs.clf), --data, $(inputs.X)]

# Command arguments

# Outputs section
outputs: []


# Running in a container
