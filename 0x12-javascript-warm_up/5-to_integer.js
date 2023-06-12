#!/usr/bin/node

process.argv.slice(2);
const firstarg = process.argv[2];

if (isNaN(firstarg)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstarg}`);
}
