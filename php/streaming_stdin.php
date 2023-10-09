<?php
// Script reads streaming input text and then prints capitalized string to stdout

while ($user_input = fgets(STDIN)) {
    echo strtoupper($user_input);
}
