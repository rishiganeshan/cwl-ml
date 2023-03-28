cwlVersion: v1.0
class: Workflow
requirements:
  - class: MultipleInputFeatureRequirement
  - class: StepInputExpressionRequirement

inputs:
  project_path: string

outputs:
  predictions:
    type: Any
    outputSource: test_predictions/predictions_output

steps:
  build_docker_image:
    run: cwlFiles/build_docker_image.cwl
    in: []
    out: [dummy_output]
  run_docker_container:
    run: cwlFiles/run_docker_container.cwl
    in:
      dummy_input: build_docker_image/dummy_output
      project_path: project_path
    out: [dummy_output]

  test_predictions:
    run: cwlFiles/test_predictions.cwl
    in:
      dummy_input: run_docker_container/dummy_output
      url: { valueFrom: "http://localhost:9001" }
    out: [predictions_output]
