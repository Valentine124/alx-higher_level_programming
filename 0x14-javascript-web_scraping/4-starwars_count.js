#!/usr/bin/node

const request = require('request');
const process = require('process');

const id = 18;
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);
  let count = 0;
  const wAntId = 'https://swapi-api.alx-tools.com/api/people/' + id + '/';

  for (const index in data.results) {
    const characters = data.results[index].characters;

    if (characters.includes(wAntId)) {
      count += 1;
    }
  }

  console.log(count);
});
