<?php
// Script to decode Base64 text

$encodedString = $argv[1];

// Decode the Base64 encoded string
$decodedString = base64_decode($encodedString);

echo $decodedString . "\n";
