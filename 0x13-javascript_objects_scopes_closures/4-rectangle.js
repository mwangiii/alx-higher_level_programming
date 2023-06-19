#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && Number.isInteger(w) && h > 0 && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0;
      this.height = 0;
    }
  }

  print () {
    if (this.width > 0 && this.height > 0) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    if (this.width > 0 && this.height > 0) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    if ((this.width > 0 && this.height > 0)) {
      [this.width, this.height] = [this.width * 2, this.height * 2];
    }
  }
}
module.exports = Rectangle;
