#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Step 1:
docker build -t project:1.0 .
# Step 2: 
# List docker images
docker image ls
# Step 3: 
# Run flask app
docker container run --name project -p 3000:80 project:1.0
