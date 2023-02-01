#!/usr/bin/node
const argList = process.argv.slice(2).filter(arg => !isNaN(parseInt(arg)));
console.log(argList.length > 1 ? Math.max(...argList.sort((a, b) => b - a).slice(1)) : 0);
