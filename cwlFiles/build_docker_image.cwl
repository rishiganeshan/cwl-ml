cwlVersion: v1.0
class: CommandLineTool

baseCommand: docker

arguments:
  - valueFrom: build
  - valueFrom: -t
  - valueFrom: my-tf-serving
  - valueFrom: --no-cache
  - valueFrom: -f
  - valueFrom: /Users/rishiganeshan/Desktop/myProject/Dockerfile
  - valueFrom: .


inputs: []

outputs:
  dummy_output:
    type: string
    outputBinding:
      outputEval: "dummy"








# cwlVersion: v1.0
# class: CommandLineTool
# baseCommand: docker
# inputs:
#   dockerfile_path:
#     type: string
#     default: /Users/rishiganeshan/Desktop/myProject/Dockerfile

# arguments:
#   - build
#   - -t
#   - my-tf-serving
#   - .
#   - -f
#   - $(inputs.dockerfile_path)

# outputs:
#   dummy_output:
#     type: string
#     outputBinding:
#       glob: "*.dummy"
#       loadContents: true
#       outputEval: $(self[0].contents)
