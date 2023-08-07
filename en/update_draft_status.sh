#!/bin/bash

DIRS=("m1/01_basics" "m1/02_uml" "m1/03_sml" "m2/01_networks" "m2/02_nlp" \
"m4/01_Intro\ to\ Deep\ Learning" "m4/02_Traditional\ neural\ network\ architectures" \
"m4/03_Intro\ to\ transformer\ models" "m4/04_Transformer" "m5/01_Legal" \
"m5/02_presentations" "m6/01_Databases" "m6/02_Big\ Data\ workflows" \
"m6/03_From\ notebook\ to\ API" "m6/04_MLOps\ with\ mlflow" "m6/05_Deployment")

for dir in "${DIRS[@]}"; do
  echo "Processing directory: $dir"
  for file in $(find "${dir}" -name '*.md'); do
    echo "Updating file: $file"
    # Read YAML front matter into a string
    front_matter=$(sed -n '/---/,/---/p' "$file")

    if grep -q "^draft: " <<< "$front_matter"; then
      # If 'draft' exists, change its value to 'true'
      sed -i 's/^draft: .*/draft: true/' "$file"
    else
      # If 'draft' does not exist, add 'draft: true' after the first line
      sed -i '1a draft: true' "$file"
    fi
  done
done
