#!/usr/bin/node

if (process.argv.length > 2) {
  const firstarg = process.argv[2];
  console.log(`${firstarg}`);
} else {
  console.log('No argument');
}
