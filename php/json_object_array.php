<?php
// Script writes an array of objects to stdout

// Get the command-line arguments into an array
$args = array_slice($argv, 1);

// Create an array of dictionaries (associative arrays), one per argument
$myArray = array_map(function($arg) {
    return [strtoupper($arg) => strlen($arg)];
}, $args);

// Encode the array as JSON and print to stdout
echo json_encode($myArray) . "\n";
