// Script takes args and turns into JSON array

const myStrings = process.argv.slice(2) // Get command-line arguments, excluding 'node' and script name

console.log(JSON.stringify(myStrings))