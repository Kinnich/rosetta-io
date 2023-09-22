// Script to read stdin line by line, transform, and write to stdout
import * as readline from 'node:readline/promises'

const rl = readline.createInterface({ input: process.stdin })

let i = 1
for await (const line of rl) {
  console.log(i, line.toUpperCase())
  i += 1
}