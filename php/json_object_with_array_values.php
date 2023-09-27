<?php
// Script takes args and transforms into python dict with arrays as dict values

// Get the command-line arguments into an array
$myStrings = array_slice($argv, 1);

// Create an associative array (dictionary) with each string as a key and an array of letters as the value
$stringLettersDict = array_combine($myStrings, array_map('str_split', $myStrings));

// Convert each letter to uppercase within the arrays
foreach ($stringLettersDict as &$lettersArray) {
    $lettersArray = array_map('strtoupper', $lettersArray);
}

// Encode the dictionary as JSON and print to stdout
echo json_encode($stringLettersDict) . PHP_EOL;
?>