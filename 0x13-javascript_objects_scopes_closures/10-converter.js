#!/usr/bin/node
exports.converter = function (base) {
  return function (a) {
    return a.toString(base);
  };
};
