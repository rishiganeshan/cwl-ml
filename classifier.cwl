cwlVersion: v1.2
class: Workflow

inputs:
  train: File
  cfg: File
steps:
  train:
    run: cwlFiles/train.cwl
    in:
      pyfile: train
    out: []
  

  
outputs: []
