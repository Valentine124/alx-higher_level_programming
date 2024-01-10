#!/usr/bin/node

const args = process.argv;

if (args.length < 3) {
  console.log(0);
} else if (args.length === 3) {
  console.log(0);
} else {
  let largest = 0;
  let secondLargest = 0;

  for (let i = 2; i < args.length; i++) {
    if (Number(args[i]) > largest) {
      secondLargest = largest;
      largest = Number(args[i]);
    }
  }

  console.log(secondLargest);
}
