#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let second = -Infinity;

  for (let i = 0; i < args.length; i++) {
    const num = args[i];

    if (num > max) {
      second = max;
      max = num;
    } else if (num > second && num < max) {
      second = num;
    }
  }

  console.log(second);
}
