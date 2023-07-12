#!/bin/bash

# Get the URL from the user and store it in variable url
read -p "Enter the URL: " url

# Send a request to the URL and store the response in a temporary file
# mktemp makes temporary files
# curl -s makes silent request
# -o saves the output to a temporary file
response=$(mktemp)
curl -s -o "$response" "$url"

# Get the size of the response body in bytes
# < "response" reads contents in the file
size=$(wc -c < "$response")

# Display the size in bytes
echo "Size of the response body: $size bytes"

# Clean up the temporary file
rm "$response"
