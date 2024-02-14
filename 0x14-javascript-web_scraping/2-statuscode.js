#!/usr/bin/node

const urlRequest = process.argv[2];

const request = require('request');

request(urlRequest, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
