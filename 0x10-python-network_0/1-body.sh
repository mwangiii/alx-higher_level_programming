#!/bin/bash

# Get the URL from the user
read -p "Enter the URL: " url

# Send a GET request to the URL and store the response in a temporary file
response=$(mktemp)
curl -s -o "$response" -w "%{http_code}" "$url"

# Get the status code from the response
status_code=$(tail -n1 "$response")

# Display the body of the response if the status code is 200
if [ "$status_code" = "200" ]; then
    cat "$response"
else
    echo "Received status code: $status_code"
fi

# Clean up the temporary file
rm "$response"
