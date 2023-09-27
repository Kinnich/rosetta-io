<?php
/* Read a file (file path given as a command line argument),
and write to stdout
*/

// Get the file path from command line arguments
$file_path = $argv[1];

// Open the file for reading
$file = fopen($file_path, 'r');

$i = 1;

while (($line = fgets($file)) !== false) {
    echo $i . ' ' . strtoupper($line);
    $i++;
}

// Close the file
fclose($file);
?>