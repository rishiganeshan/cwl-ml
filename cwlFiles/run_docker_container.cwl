cwlVersion: v1.0
class: CommandLineTool
baseCommand: docker
requirements:
  - class: InlineJavascriptRequirement
arguments:
  - run
  - --name
  - myTFServing
  - -d
  - -v
  - (inputs.project_path)/myProject:/myProject
  - -p
  - 9001:9001
  - my-tf-serving
inputs:
  project_path: string
  dummy_input: string
outputs:
  dummy_output:
    type: string
    outputBinding:
      outputEval: "dummy"
