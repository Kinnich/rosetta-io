<?php
// Script reads string args and transforms into python dict

// Get the command-line arguments into an array
$myStrings = array_slice($argv, 1);

// Create an associative array (dictionary) with each string as a key and its length as the value
$stringLengthDict = array_combine($myStrings, array_map('strlen', $myStrings));

// Encode the dictionary as JSON and print to stdout
echo json_encode($stringLengthDict) . "\n";
