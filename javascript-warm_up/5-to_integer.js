#!/usr/bin/node
const args = process.argv.slice(2);

const argc = parseInt(args[0]);

if (Number.isNaN(argc)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argc}`);
}
