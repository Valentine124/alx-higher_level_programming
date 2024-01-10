#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      if (w === undefined || h === undefined) return;
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let outer = 0;
    let inner = 0;

    while (outer < this.height) {
      let str = '';

      while (inner < this.width) {
        str += 'X';
        inner += 1;
      }

      inner = 0;
      console.log(str);
      outer += 1;
    }
  }
};
