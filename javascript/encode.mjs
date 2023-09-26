// Script to encode a string as Base64

const testString = process.argv[2] // Get the Base64-encoded string from command-line arguments

const encodedString = btoa(testString)

console.log(encodedString)