// Read a file (file path given as a command line argument),
// and write to stdout
import * as readline from 'node:readline/promises'
import fs  from 'fs'


// Get the file path from the command-line argument
const file_path = process.argv[2]

const lines = []

const rl = readline.createInterface({
  input: fs.createReadStream(file_path),
  crlfDelay: Infinity, // To recognize both '\n' and '\r\n' as line terminators
})

rl.on('line', (line) => {
  lines.push(line)
})

rl.on('close', () => {
  let i = 1
  lines.forEach(line => {
    console.log(i + " " + line.toUpperCase())
    i++
  })
})