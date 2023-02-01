#!/usr/bin/node
const add = (a, b) => {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
};

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
