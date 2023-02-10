#!/usr/bin/node

const dictInput = require('./101-data').dict;
const outDict = {};

for (const key in dictInput) {
  const occur = dictInput[key];
  outDict[occur] = [];
  for (const keys in dictInput) {
    if (dictInput[keys] === occur) {
      outDict[occur].push(keys);
    }
  }
}
console.log(outDict);
