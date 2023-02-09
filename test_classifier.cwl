# File header
cwlVersion: v1.2
class: CommandLineTool

# Command line tool inputs
inputs:
    pyfile: File
    test_data: File
    clf: File

# Specifying the program to run
baseCommand: [python3]

arguments: [$(inputs.pyfile), --classifier, $(inputs.clf), --data, $(inputs.test_data)]

# Command arguments

# Outputs section
outputs: []


# Running in a container
