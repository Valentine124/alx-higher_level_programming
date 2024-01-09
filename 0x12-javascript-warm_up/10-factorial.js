#!/usr/bin/node

function factoria (num) {
  if (num === 1) return 1;
  else return num * factoria(num - 1);
}

const num = Number(process.argv[2]);

if (!num) console.log(1);
else console.log(factoria(num));
