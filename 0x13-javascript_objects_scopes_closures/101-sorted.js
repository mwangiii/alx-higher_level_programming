#!/usr/bin/node

// Importing the dict dictionary from the 101-data.js file
const { dict } = require('./101-data');

// Computing a new dictionary of user IDs by occurrence
const newDict = {};

for (const userId in dict) {
  const occurrence = dict[userId];

  if (newDict[occurrence]) {
    newDict[occurrence].push(userId);
  } else {
    newDict[occurrence] = [userId];
  }
}

// Printing the new dictionary
console.log(newDict);
