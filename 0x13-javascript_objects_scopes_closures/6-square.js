#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) this.print();
    else {
      let outer = 0;
      let inner = 0;

      while (outer < this.height) {
        let str = '';

        while (inner < this.width) {
          str += c;
          inner += 1;
        }

        inner = 0;
        console.log(str);
        outer += 1;
      }
    }
  }
};
