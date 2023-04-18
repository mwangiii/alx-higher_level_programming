#!/usr/bin/node

const arg = process.argv.slice(2);

if (arg === 1) {
  console.log(arg);
} else {
  console.log('No argument');
}
