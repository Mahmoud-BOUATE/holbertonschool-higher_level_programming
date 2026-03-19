#!/usr/bin/node

const size = Number(process.argv[2]);

if (Number.isNaN(size)) {
  console.log('Missing size');
} else if (size > 0) {
  let i = 0;

  while (i < size) {
    let j = 0;
    let line = '';

    while (j < size) {
      line += 'X';
      j++;
    }

    console.log(line);
    i++;
  }
}
