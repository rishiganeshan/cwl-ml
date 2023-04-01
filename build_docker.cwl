cwlVersion: v1.0
class: CommandLineTool

requirements:
  InlineJavascriptRequirement: {}
  DockerRequirement:
    dockerPull: docker

baseCommand: ["docker", "build"]

inputs:
  context:
    type: Directory
    inputBinding:
      position: 1
      prefix: --file
      valueFrom: $(inputs.context.path + "/Dockerfile")
  tag:
    type: string
    inputBinding:
      position: 2
      prefix: -t

outputs:
  docker_build_log:
    type: stdout
  dummy: 
    type: string
    outputBinding:
      outputEval: "dummy"
      
      
    
stdout: docker_build_log.txt
