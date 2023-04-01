cwlVersion: v1.0
class: Workflow



outputs:
  saved_models:
    type: Directory
    outputSource: train_step/saved_models
  predictions:
    type: File
    outputSource: deploy_step/predictions

inputs:
  train_script: File

steps:
  train_step:
    run: train.cwl
    in:
      train_script: train_script
    out: [saved_models]


  deploy_step:
    run: deploy.cwl
    in:
      saved_models: train_step/saved_models
    out: [predictions]
