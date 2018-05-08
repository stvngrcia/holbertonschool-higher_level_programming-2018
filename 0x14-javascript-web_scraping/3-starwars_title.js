#!/usr/bin/node

let request = require('request');
let episode = process.argv[2];
let url = 'http://swapi.co/api/films/' + episode;

request(url, function (err, data, body) {
  if (err) throw err;
  console.log(JSON.parse(body)['title']);
});
