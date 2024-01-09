#!/usr/bin/node

const num = Number(process.argv[2]);
let count = 0;
let inner = 0;

if (!num) {
  console.log('Missing size');
} else {
  while (count < num) {
    let str = '';
    while (inner < num) {
      str += 'X';
      inner += 1;
    }
    inner = 0;
    console.log(str);
    count += 1;
  }
}
