#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let j = 0; i < size; j++) {
    let row = '';
    for (let k = 0; k < size; k++) {
      row += 'X';
    }
    console.log(row);
  }
}
