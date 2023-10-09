<?php
// Script takes args and turns into JSON array

// Get the command-line arguments into an array
$myStrings = array_slice($argv, 1);

// Encode the array as JSON and print to stdout
echo json_encode($myStrings) . "\n";
