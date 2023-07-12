#!/bin/bash

# Check if the URL argument is provided
# $1 is the first argument
# -z checks if the string is empty
if [ -z "$1" ]; then
  echo "URL argument is missing"
  exit 1
fi

# Extract the URL from the first argument
url="$1"

# Send a GET request to the URL with the custom header and store the response in a temporary file
# -H sets a custom  header
response=$(mktemp)
curl -s -o "$response" -H "X-School-User-Id: 98" "$url"

# Display the body of the response
cat "$response"

# Clean up the temporary file
rm "$response"
