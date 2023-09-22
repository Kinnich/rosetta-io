// Script writes an array of objects to stdout

const args = process.argv.slice(2)

// Make a list of dictionaries from the given args, one dict per arg
const myArray = args.map((arg) => ({ [arg.toUpperCase()]: arg.length }))

console.log(JSON.stringify(myArray))