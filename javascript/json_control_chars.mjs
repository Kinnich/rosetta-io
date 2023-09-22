// Script takes control characters and outputs valid JSON

const myString = process.argv[2]

console.log(JSON.stringify(myString))