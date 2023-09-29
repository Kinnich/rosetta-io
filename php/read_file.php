<?php
/* Read a file (file path given as a command line argument),
and write to stdout
*/

// Get the file path from command line arguments
$file_path = $argv[1];

// Open the file for reading
$file = fopen($file_path, 'r');

foreach (file($file_path) as $index => $line) {
    echo ($index + 1) . ' ' . strtoupper($line);
}
