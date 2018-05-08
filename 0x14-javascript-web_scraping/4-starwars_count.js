#!/usr/bin/node
let request = require('request');
let url = process.argv[2];

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let counter = 0;
    let films = JSON.parse(body).results;
    for (let result = 0; result < films.length; result++) {
      let characters = films[result]['characters'];
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === 'https://swapi.co/api/people/18/' || characters[j] === 'http://swapi.co/api/people/18/') {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
