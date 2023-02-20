# File header
cwlVersion: v1.2
class: CommandLineTool

# Command line tool inputs
inputs:
    pyfile: File
    model: File
    class_names: File

# Specifying the program to run
baseCommand: [python3]

arguments: [$(inputs.pyfile), --model, $(inputs.model), 
--class_names, $(inputs.class_names)]

# Command arguments

# Outputs section
outputs: []
    

# Running in a container
