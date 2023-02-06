#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], 'utf-8', function (error, content) {
  console.log(error || content);
});
