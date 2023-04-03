cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "make_requests.py"]
requirements:
  DockerRequirement:
    dockerImageId: custom
    dockerFile: 
      $include: Dockerfile
inputs:
  make_requests_script:
    type: File
  dummy:
    type: string
# outputs: []
outputs:
  predictions:
    type: File
    outputBinding:
      glob: "predictions.txt"



