#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg);

if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let output = '';
  let i = 0;
  while (i < x) {
    output += 'C is fun\n';
    i++;
  }
  console.log(output.trim());
}
