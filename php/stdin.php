<?php
// Script to read stdin line by line, transform, and return it

$i = 1;

while ($user_input = fgets(STDIN)) { // fgets returns false when nothing left to read
    echo $i++ . ' ' . strtoupper($user_input);
}
