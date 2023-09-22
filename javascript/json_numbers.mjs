// Script takes args and outputs a list of lengths

const myStrings = process.argv.slice(2)

// Create an array of numbers based on the length of the string args
const stringLengths = myStrings.map((string) => string.length)

const jsonString = JSON.stringify(stringLengths)

console.log(jsonString)