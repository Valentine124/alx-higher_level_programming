#!/usr/bin/node

exports.logMe = function (item) {
  let staticVar = 0;

  console.log(staticVar + ': ' + item);
  return function () {
    ++staticVar;
  }
}
