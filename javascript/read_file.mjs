// Read a file (file path given as a command line argument),
// and write to stdout
import * as readline from 'node:readline/promises'
import fs  from 'fs'


// Get the file path from the command-line argument
const file_path = process.argv[2]

const rl = readline.createInterface({
  input: fs.createReadStream(file_path),
})

let i = 1
for await (const line of rl) {
  console.log(i + " " + line.toUpperCase())
  i++
}