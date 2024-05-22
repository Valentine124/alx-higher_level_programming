#!/usr/bin/node

const process = require('process');
const fs = require('fs');

let PATH = process.argv[2];

fs.readFile(PATH, function (err, data) {
	if (err) {
		console.error(err);
		return;
	}
	console.log(data.toString());
});
