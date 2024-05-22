#!/usr/bin/node

const process = require('process');
const request = require('request');

const URL = process.argv[2];

request
  .get(URL)
  .on('response', response => {
    console.log('code: ' + response.statusCode);
  });
