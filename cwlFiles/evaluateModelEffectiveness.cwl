# File header
cwlVersion: v1.2
class: CommandLineTool

# Command line tool inputs
inputs:
    pyfile: File
    model: File
    ds_test: File

# Specifying the program to run
baseCommand: [python3]

arguments: [$(inputs.pyfile), --model, $(inputs.model), 
--ds_test, $(inputs.ds_test)]

# Command arguments

# Outputs section
outputs: []
    

# Running in a container
