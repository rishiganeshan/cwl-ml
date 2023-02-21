cwlVersion: v1.2
class: Workflow

inputs:
  importData: File
  buildModel: File
  trainModel: File
  evaluateModelEffectiveness: File
  makePredictions: File

steps:
  importData:
    run: cwlFiles/importData.cwl
    in:
      pyfile: importData
    out: [features, labels, ds_test, class_names, ds_train_batch]
  buildModel:
    run: cwlFiles/buildModel.cwl
    in: 
      pyfile: buildModel
      features: importData/features
      labels: importData/labels
    out: [model]
  trainModel:
    run: cwlFiles/trainModel.cwl
    in:
      pyfile: trainModel
      features: importData/features
      labels: importData/labels
      model: buildModel/model
      ds_train_batch: importData/ds_train_batch
    out: [model]
  evaluateModelEffectiveness:
    run: cwlFiles/evaluateModelEffectiveness.cwl
    in:
      pyfile: evaluateModelEffectiveness
      model: trainModel/model
      ds_test: importData/ds_test
    out: []
  makePredictions:
    run: cwlFiles/makePredictions.cwl
    in:
      pyfile: makePredictions
      model: trainModel/model
      class_names: importData/class_names
    out: []

  
outputs: []
