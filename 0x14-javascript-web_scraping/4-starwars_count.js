#!/usr/bin/node
let request = require('request');
let url = process.argv[2];
let counter = 0;
if (url !== undefined) {
  request(url, function (err, data, body) {
    if (err) {
      console.log(counter);
      console.log(err);
    }
    if (url === 'http://swapi.co/api/films') {
      let films = JSON.parse(body).results;
      for (let result = 0; result < films.length; result++) {
        for (let char = 0; char < films[result]['characters'].length; char++) {
          if (films[result]['characters'][char] === 'https://swapi.co/api/people/18/') {
            counter += 1;
          }
        }
      }
    }
    console.log(counter);
  });
}
