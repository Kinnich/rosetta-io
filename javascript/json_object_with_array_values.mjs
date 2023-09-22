// Script takes command line args and transforms into python dict with arrays as dict values

const myStrings = process.argv.slice(2)

const stringLettersDict = {}

for (const string of myStrings) {
    const uppercaseLetters = [...string].map((s) => s.toUpperCase())
    stringLettersDict[string] = uppercaseLetters
}

console.log(JSON.stringify(stringLettersDict))