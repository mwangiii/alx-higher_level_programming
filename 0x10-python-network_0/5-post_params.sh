#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
  echo "URL argument is missing"
  exit 1
fi

# Extract the URL from the first argument
url="$1"

# Set the variables for the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Send a POST request to the URL with the custom variables and store the response in a temporary file
# -d sets the body of the request
response=$(mktemp)
curl -s -o "$response" -d "email=$email&subject=$subject" "$url"

# Display the body of the response
cat "$response"

# Clean up the temporary file
rm "$response"
