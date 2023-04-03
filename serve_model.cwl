cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "serve_model.py"]
requirements:
  DockerRequirement:
    dockerImageId: custom
    dockerFile: 
      $include: Dockerfile
  InitialWorkDirRequirement:
    listing:
      - entryname: "serve_model.py"
        entry: $(inputs.serve_model_script)
inputs:
  serve_model_script:
    type: File
    # inputBinding:
    #   position: 1
    #   prefix: ""
outputs:
  dummy:
    type: string
    outputBinding:
      outputEval: "dummy"
    

