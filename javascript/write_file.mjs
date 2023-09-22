// Script to write text to a new file
import fs from 'fs/promises'

const [outfile, text] = process.argv.slice(2) // Get command-line arguments

await fs.writeFile(outfile, text.toUpperCase())