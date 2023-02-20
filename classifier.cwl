cwlVersion: v1.2
class: Workflow

inputs:
  importData: File
  buildModel: File
  trainModel: File
  createOptimiser: File
  evaluateModelEffectiveness: File
  makePredictions: File

steps:
  importData:
    run: cwlFiles/importData.cwl
    in:
      pyfile: importData
    out: [features, labels, ds_test, class_names]
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
    out: [model]
  createOptimiser:
    run: cwlFiles/createOptimiser.cwl
    in:
      pyfile: createOptimiser
      features: importData/features
      labels: importData/labels
      model: trainModel/model
    out: [model]
  evaluateModelEffectiveness:
    run: cwlFiles/evaluateModelEffectiveness.cwl
    in:
      pyfile: evaluateModelEffectiveness
      model: createOptimiser/model
      ds_test: importData/ds_test
    out: []
  makePredictions:
    run: cwlFiles/makePredictions.cwl
    in:
      pyfile: makePredictions
      model: createOptimiser/model
      class_names: importData/class_names
    out: []

  
outputs: []
