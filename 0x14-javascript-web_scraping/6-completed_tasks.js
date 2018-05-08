#!/usr/bin/node
let request = require('request');
let url = process.argv[2];
let myDict = {};

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let response = JSON.parse(body);

    for (let i = 0; i < response.length; i++) {
      if (response[i]['completed'] === true) {
        if (myDict[response[i]['userId']] === undefined) {
          myDict[response[i]['userId']] = 1;
        } else {
          myDict[response[i]['userId']] += 1;
        }
      }
    }
  }
  console.log(myDict);
});
