<?php
// Script takes args and outputs a list of lengths

// Get the command-line arguments into an array
$myStrings = array_slice($argv, 1);

// Create an array of numbers based on the length of the string args
$stringLengths = array_map('strlen', $myStrings);

// Encode the array as JSON and print to stdout
echo json_encode($stringLengths) . PHP_EOL;
?>