cwlVersion: v1.0
class: Workflow


requirements:
  DockerRequirement:
    dockerImageId: custom
    dockerFile: 
      $include: Dockerfile
outputs:
  saved_models:
    type: Directory
    outputSource: train_step/saved_models
  predictions:
    type: File
    outputSource: make_requests/predictions

inputs:
  train_script: File
  serve_model_script:
    type: File
  make_requests_script:
    type: File

steps:
  train_step:
    run: train.cwl
    in:
      train_script: train_script
    out: [saved_models]
  serve_model:
    run: serve_model.cwl
    in:
      serve_model_script: serve_model_script
    out: [dummy]
  make_requests:
    run: make_requests.cwl
    in:
      make_requests_script: make_requests_script
      dummy: serve_model/dummy
    # out: []
    out: [predictions]


  # deploy_step:
  #   run: deploy.cwl
  #   in:
  #     deploy_script: deploy_script
  #     saved_models: train_step/saved_models
  #   out: [predictions]

  # tensorflow_serving_step:
  #   run: tensorflow_serving.cwl
  #   in:
  #     saved_models: train_step/saved_models
  #   out: [tensorflow_serving_log]
