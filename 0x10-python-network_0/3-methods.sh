#!/bin/bash

# Get the URL from the user
read -p "Enter the URL: " url

# Send an OPTIONS request to the URL and store the response headers in a temporary file
# -X sets HTTP method to OPTIONS
# -I tells curl to ignore the response body
response=$(mktemp)
curl -s -o "$response" -X OPTIONS -I "$url"

# Extract the Allow header from the response
# -i ignores case
# result is stored in allow_header
allow_header=$(grep -i "^Allow:" "$response" | sed -e 's/Allow: //i')

# Display the HTTP methods accepted by the server
echo "HTTP methods accepted by the server:"
echo "$allow_header"

# Clean up the temporary file
rm "$response"
