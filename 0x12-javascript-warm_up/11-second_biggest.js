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
    let flag = 0;

    if (Number(args[i]) > largest) {
      flag = 1;
      secondLargest = largest;
      largest = Number(args[i]);
    }

    if (!flag) {
      if (Number(args[i]) > secondLargest) {
        secondLargest = Number(args[i]);
      }
    }
  }

  console.log(secondLargest);
}
