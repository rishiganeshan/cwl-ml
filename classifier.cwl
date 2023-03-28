cwlVersion: v1.0
class: Workflow
requirements:
  - class: InlineJavascriptRequirement

inputs:
  project_path: string
  config_file: File
  rest_api_port: int

outputs:
  server_logs:
    type: File
    outputSource: run_tf_serving/logs

steps:
  run_tf_serving:
    run:
      class: CommandLineTool
      baseCommand: [docker, run]
      arguments:
        - --rm
        - --name
        - myTFServing
        - -v
        - $(inputs.project_path):/myProject
        - -p
        - $(inputs.rest_api_port):$(inputs.rest_api_port)
        - tensorflow/serving
        - /usr/bin/tensorflow_model_server
        - --rest_api_port=$(inputs.rest_api_port)
        - --model_config_file=/myProject/$(inputs.config_file.basename)
        - --allow_version_labels_for_unavailable_models
      inputs:
        project_path: string
        config_file: File
        rest_api_port: int
      outputs:
        logs:
          type: stdout
      stdout: server_logs.txt
      requirements:
        - class: DockerRequirement
          dockerPull: "tensorflow/serving"
    in:
      project_path: project_path
      config_file: config_file
      rest_api_port: rest_api_port
    out: [logs]
