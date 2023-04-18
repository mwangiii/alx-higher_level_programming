#!/usr/bin/node
const arg = process.argv.slice(2);
if (parseInt(arg)) {
  console.log(`My number: '${arg[0]}'`);
} else {
  console.log('Not a number');
}
