#!/usr/bin/node

if (process.argv.slice(2)) {
  const firstarg = process.argv[2];
  const secongarg = process.argv[3];
  console.log(`${firstarg} is ${secongarg}`);
}
