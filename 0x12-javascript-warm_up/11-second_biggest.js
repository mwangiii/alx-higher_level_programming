#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);

    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num !== largest) {
      secondLargest = num;
    }
  }

  console.log(secondLargest);
}
