#!/usr/bin/node
const process = require('process');
let num = parseInt(process.argv[2]);
const msg1 = 'Missing number of occurrences';
const msg2 = 'C is fun';
if (isNaN(num)) {
  console.log(msg1);
} else {
  while (num > 0) {
    console.log(msg2);
    num--;
  }
}
