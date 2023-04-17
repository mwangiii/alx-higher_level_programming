#!/usr/bin/node
const args = process.argv.length;

if (process.args === 0) {
  console.log('No argument');
} else if (process.args === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
