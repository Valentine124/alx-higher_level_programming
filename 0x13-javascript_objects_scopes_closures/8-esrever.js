#!/usr/bin/node

exports.esrever = function (list) {
  const arr = [];
  let idx = 0;
  const idx2 = list.length;

  for (let i = idx2 - 1; i >= 0; i--) {
    arr[idx] = list[i];
    idx += 1;
  }

  return arr;
};
