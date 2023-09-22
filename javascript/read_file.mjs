// Read a file (file path given as a command line argument),
// and write to stdout


import * as readline from 'node:readline/promises'
import fs  from 'fs';


const file_path = process.argv[2]; // Get the file path from the command-line argument

const lines = [];

const rl = readline.createInterface({
  input: fs.createReadStream(file_path),
  crlfDelay: Infinity, // To recognize both '\n' and '\r\n' as line terminators
});

let i = 1;
rl.on('line', (line) => {
  lines.push(i + " " + line.toUpperCase());
  i++
});

rl.on('close', () => {
  lines.forEach(line => {
    console.log(line)
  })
});




