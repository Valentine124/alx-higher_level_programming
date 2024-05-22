#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const request = require('request');

const URL = process.argv[2];
const PATH = process.argv[3];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  fs.writeFile(PATH, body, err => {
    if (err) {
      console.log(err);
    }
  });
});
