#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter((n) => n === searchElement).length;
};
