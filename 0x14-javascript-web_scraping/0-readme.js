#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const PATH = process.argv[2];

fs.readFile(PATH, 'utf-8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data.toString());
});
