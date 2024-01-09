#!/usr/bin/node

const num = Number(process.argv[2]);
let count = 0;

if (!num) {
  console.log('Missing number of occurrences');
} else {
  while (count < num) {
    console.log('C is fun');
    count += 1;
  }
}
