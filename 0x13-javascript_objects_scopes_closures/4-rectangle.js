#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let myRow = '';
      for (let j = 0; j < this.width; j++) {
        myRow += 'X';
      }
      console.log(myRow);
    }
  }
  rotate () {
    let tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }
  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
