#!/usr/bin/node

let request = require('request');
let episode = process.argv[2];
let url = 'http://swapi.co/api/films/' + episode;

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body)['title']);
  }
});
