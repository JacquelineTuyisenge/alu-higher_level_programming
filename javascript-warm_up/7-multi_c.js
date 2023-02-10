#!/usr/bin/node
let x = process.argv[2];
let i = 0;

if (!Number.isInteger(Number(x))) {
  console.log('Missing number of occurrences');
} else {
  x = Number(x);
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
