#!/usr/bin/node
const process = require('process');
const x = parseInt(process.argv[2]);
const msg = 'Missing size';
if (isNaN(x)) {
  console.log(msg);
} else {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
}