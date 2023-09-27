<?php
// Write text to a new file

// Get command-line arguments
$outfile = $argv[1];
$text = $argv[2];

// Convert the text to uppercase
$uppercaseText = strtoupper($text);

// Write the uppercase text to the specified file
file_put_contents($outfile, $uppercaseText);
?>