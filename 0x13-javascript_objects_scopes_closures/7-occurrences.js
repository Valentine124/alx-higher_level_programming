#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let idx = 0;

  while (list[idx]) {
    if (list[idx] === searchElement) count += 1;
    idx += 1;
  }

  return count;
};
