#!/usr/bin/node

const sec = process.argv[2];
const num = Number(sec);

if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
