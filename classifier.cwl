cwlVersion: v1.2
class: Workflow

inputs:
  raw_data: File
  load_data_pyfile: File
  load_test_data_pyfile: File
  train_pyfile: File
  test_pyfile: File
  test_data: File
steps:
  load_data:
    run: load_data.cwl
    in: 
      data: raw_data
      pyfile: load_data_pyfile
    out: [labelled_data]
  load_test_data:
    run: load_test_data.cwl
    in: 
      data: test_data
      pyfile: load_test_data_pyfile
    out: [labelled_test_data]
  train:
    run: train_classifier.cwl
    in:
      data: load_data/labelled_data
      pyfile: train_pyfile
    out: [clf]
  test:
    run: test_classifier.cwl
    in:
      pyfile: test_pyfile
      test_data: load_test_data/labelled_test_data
      clf: train/clf
    out: []

  
outputs: []
