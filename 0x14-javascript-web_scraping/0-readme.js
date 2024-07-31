#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const PATH = process.argv[2];

fs.readFile(PATH, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
