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
    out: [features, labels, np_test, class_names, np_train_batch]
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
      np_train_batch: importData/np_train_batch
    out: [model]
  evaluateModelEffectiveness:
    run: cwlFiles/evaluateModelEffectiveness.cwl
    in:
      pyfile: evaluateModelEffectiveness
      model: trainModel/model
      np_test: importData/np_test
    out: []
  makePredictions:
    run: cwlFiles/makePredictions.cwl
    in:
      pyfile: makePredictions
      model: trainModel/model
      class_names: importData/class_names
    out: []

  
outputs: []
