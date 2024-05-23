#!/usr/bin/node

const process = require('process');
const request = require('request');

const id = process.argv[2];
const URL = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const result = JSON.parse(body);

  for (const idx in result.characters) {
    request(result.characters[idx], (error, response, body) => {
      if (error) {
        console.log(error);
      }

      const data = JSON.parse(body);

      console.log(data.name);
    });
  }
});
