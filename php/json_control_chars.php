<?php
// Script takes control characters and outputs valid JSON

// Get the command-line argument
$testString = $argv[1];

// Cast the string to JSON and print to stdout
echo json_encode($testString) . "\n";
