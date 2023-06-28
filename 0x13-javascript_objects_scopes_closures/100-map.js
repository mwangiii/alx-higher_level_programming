#!/usr/bin/node

// Importing the list array from the 100-data.js file
const { list } = require('./100-data');

// Computing a new array using the map function
const newArray = list.map((value, index) => value * index);

// Printing the initial list and the new array
console.log('Initial List:', list);
console.log('New Array:', newArray);
