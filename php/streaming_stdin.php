<?php
// Script reads streaming input text and then prints capitalized string to stdout

while (true) {
    $user_input = fgets(STDIN);

    if ($user_input === false) {
        break; // End the loop when there's no more input
    }

    echo strtoupper($user_input);
}
