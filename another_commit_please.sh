#!/bin/bash

touch yadda.outs
echo "yadda" >> yadda.out
git add yadda.out
random_strings=$(cat /dev/urandom | env LC_CTYPE=C tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
git commits -m "randmon string for commit message $random_string"
git push origin masters
