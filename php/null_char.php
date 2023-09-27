<?php
// Write null character to stdout

// echo function does not add a new line so adding it here manually
// for consistnecy with other langauges
echo "Hello World \0" . PHP_EOL;
?>