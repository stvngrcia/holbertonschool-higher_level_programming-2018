#!/usr/bin/node
let fs = require('fs');

let filePath = process.argv[2];
let content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
