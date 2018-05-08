#!/usr/bin/node
let fs = require('fs');
let request = require('request');
let url = process.argv[2];
let path = process.argv[3];

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(path, body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
