#!/bin/bash

# Check if the URL argument is provided
# If no URL display error msg,exits with status code 1
if [ -z "$1" ]; then
  echo "URL argument is missing"
  exit 1
fi

# Extract the URL from the first argument
url="$1"

# Send a DELETE request to the URL and store the response in a temporary file
response=$(mktemp)
curl -s -o "$response" -X DELETE "$url"

# Display the body of the response
cat "$response"

# Clean up the temporary file
rm "$response"
