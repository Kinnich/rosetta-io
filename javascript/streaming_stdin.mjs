// Script reads streaming input text and then prints capitalized string to stdout

import * as readline from 'node:readline/promises'

const rl = readline.createInterface({ input: process.stdin })

for await (const line of rl) {
  console.log(line.toUpperCase())
}