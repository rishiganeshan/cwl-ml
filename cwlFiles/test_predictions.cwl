cwlVersion: v1.0
class: CommandLineTool

baseCommand: [sh, -c]

inputs:
  url: string
  sleep_duration:
    type: int
    default: 10
  dummy_input: string
  

outputs:
  predictions_output:
    type: Any
    outputBinding:
      glob: predictions.json

arguments:
  - valueFrom: "sleep $(inputs.sleep_duration) && curl -X POST $(inputs.url)/v1/models/regression_experiments:predict -H 'Content-Type: application/json' -d '{\"instances\":[[1.0], [2.0], [5.0]]}' > predictions.json"

stdout: predictions.json
