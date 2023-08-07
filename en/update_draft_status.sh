#!/bin/bash

# Directory list
declare -a dirs=("m1/01_basics" "m1/02_uml" "m1/03_sml"
                 "m2/01_networks" "m2/02_nlp"
                 "m4/01_Intro to Deep Learning" "m4/02_Traditional neural network architectures" 
                 "m4/03_Intro to transformer models" "m4/04_Transformer"
                 "m5/01_Legal" "m5/02_presentations"
                 "m6/01_Databases" "m6/02_Big Data workflows" "m6/03_From notebook to API"
                 "m6/04_MLOps with mlflow" "m6/05_Deployment")

# For each directory
for dir in "${dirs[@]}"; do
    echo "Processing directory: $dir"
    # Find all .md files in directory
    for file in $(find $dir -name '*.md'); do
        echo "Updating file: $file"
        # Use yq to update or insert the draft field
        yq e '.draft = true' -i $file
    done
done
