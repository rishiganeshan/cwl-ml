cwlVersion: v1.2
class: Workflow

inputs:
  train_pyfile: File
  test_pyfile: File
  test_data_X: float[]
steps:
  train:
    run: train_classifier.cwl
    in:
      pyfile: train_pyfile
    out: [clf]
  test:
    run: test_classifier.cwl
    in:
      pyfile: test_pyfile
      X: test_data_X
      clf: train/clf
    out: []

  
outputs: []
