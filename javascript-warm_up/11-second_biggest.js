#!/usr/bin/node

const args = process.argv
  .slice(2)
  .map(Number);

const unique = [...new Set(args)];

unique.sort((a, b) => b - a);

if (unique.length < 2) {
  console.log(0);
} else {
  console.log(unique[1]);
}
