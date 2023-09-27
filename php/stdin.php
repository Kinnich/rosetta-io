<?php
// Script to read stdin line by line, transform, and return it

$i = 1;

while (true) {
    $user_input = fgets(STDIN);

    if ($user_input === false) {
        break; // End the loop when there's no more input
    }

    echo $i . ' ' . strtoupper($user_input);
    $i++;
}
?>
