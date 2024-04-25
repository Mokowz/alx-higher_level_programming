#!/usr/bin/node
const process = require('process');
let number;
let msg = 'Not a number';

if (process.argv.length > 2) {
  number = parseInt(process.argv[2]);
  if (!isNaN(number)) {
    number = String(number);
    msg = `My number: ${number}`;
  }
}

console.log(msg);
