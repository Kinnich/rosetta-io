<?php
// Read JSON file, transform, and print to stdout


$jsonFile = $argv[1];

// Read JSON data from the file
$jsonData = file_get_contents($jsonFile);

// Parse JSON data
$people = json_decode($jsonData);

foreach ($people as $person) {
    echo "Hello, {$person->age} year old {$person->first_name}\n";
}
