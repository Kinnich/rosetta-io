// Script takes args and turns into JSON array

const myStrings = process.argv.slice(2) // Get command-line arguments, excluding 'node' and script name

const jsonString = JSON.stringify(myStrings)

console.log(jsonString)