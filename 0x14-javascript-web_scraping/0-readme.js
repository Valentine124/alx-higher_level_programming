#!/usr/bin/node

const fs = require('fs').promises;

let PATH = process.argv[1];

fs.readFile(PATH, function (err, data) {
	if (err) {
		return console.error(error);
	}
	console.log(data.toString());
}
