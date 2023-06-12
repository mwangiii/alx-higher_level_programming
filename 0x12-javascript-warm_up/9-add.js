#!/usr/bin/node

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const firstInteger = Number(process.argv[2]);
const secondInteger = Number(process.argv[3]);

if (Number.isNaN(firstInteger) || Number.isNaN(secondInteger)) {
  console.log('NaN');
} else {
  add(firstInteger, secondInteger);
}
