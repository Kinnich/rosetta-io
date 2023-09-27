<?php
// Script to encode a string as Base64

$stringToEncode = $argv[1];

// Encode the string as Base64
$encodedString = base64_encode($stringToEncode);

echo $encodedString;
?>

