#!/bin/bash
peoples="$(cut -f 1 --output-delimiter=$'\n' people)"

while read person
do
#echo "Trying: $person"
echo "$person" | $(command -v md5 || command -v md5sum) | grep -qif /dev/stdin ../encoded && echo "$person CORRECT\! GREAT WORK, GUMSHOE."
done <<< "$peoples"


