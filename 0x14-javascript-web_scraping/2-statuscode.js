#!/usr/bin/node

let request = require('request');
let url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response['statusCode']);
  }
});
