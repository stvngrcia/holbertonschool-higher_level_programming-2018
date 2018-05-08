#!/usr/bin/node
var counter = 0;
exports.logMe = function (item) {
  console.log(counter + ': ' + item);
  counter += 1;
};
