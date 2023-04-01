# deploy.cwl
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python"]

requirements:
  DockerRequirement:
    dockerImageId: custom
    dockerFile: 
      $include: Dockerfile

inputs:
  deploy_script:
    type: File
    inputBinding:
      position: 1
  saved_models:
    type: Directory
    inputBinding:
      position: 2

outputs:
  predictions:
    type: File
    outputBinding:
      glob: "predictions.csv"

stdout: deploy.log