cwlVersion: v1.2
class: Workflow

inputs:
  train_pyfile: File
  test_pyfile: File

steps:
  train:
    run: train_classifier.cwl
    in:
      pyfile: train_pyfile
    out: []
  test:
    run: test_classifier.cwl
    in:
      pyfile: test_pyfile
    out: []

  
outputs: []
