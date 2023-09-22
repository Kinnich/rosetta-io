// Read JSON file, transform and print to stdout
import fs from 'fs/promises'

const jsonFile = process.argv[2]

const data = await fs.readFile(jsonFile, 'utf8')
const people = JSON.parse(data)

for (const person of people) {
  console.log(`Hello, ${person.age} year old ${person.first_name}`)
}