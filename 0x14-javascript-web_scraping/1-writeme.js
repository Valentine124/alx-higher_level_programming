#!/usr/bin/node

const process = require('process');
const fs = require('fs');

const PATH = process.argv[2];
const string = process.argv[3];

fs.writeFile(PATH, string, err => {
  if (err) {
    console.error(err);
  }
});
