#!/usr/bin/node

if (process.argv.slice(2)[0]){
  const firstarg = process.argv[2];
  console.log(`${firstarg}`);
} else {
  console.log('No argument');
}
