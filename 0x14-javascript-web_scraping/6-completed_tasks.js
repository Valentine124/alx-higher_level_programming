#!/usr/bin/node

const process = require('process');
const request = require('request');

const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  }

  const data = JSON.parse(body);

  const last = data.length - 1;
  let uId = data[0].userId;
  let noCompleted = 0;

  for (const idx in data) {
    if (uId === data[idx].userId) {
      if (data[idx].completed) {
        noCompleted += 1;

        continue;
      }
    } else {
      if (noCompleted !== 0) {
        if (uId === data[0].userId) {
          console.log('{ \'' + uId + '\': ' + noCompleted + ',');
        } else {
          console.log('  \'' + uId + '\': ' + noCompleted + ',');
        }
      }
      uId = data[idx].userId;
      noCompleted = 0;

      if (data[idx].completed) {
        noCompleted += 1;
      }

      if (idx === last && noCompleted !== 0) {
        console.log('  \'' + uId + '\': ' + noCompleted + ' }');
      }

      continue;
    }
  }

  if (noCompleted !== 0) {
    console.log('  \'' + uId + '\': ' + noCompleted + ' }');
  }
});
