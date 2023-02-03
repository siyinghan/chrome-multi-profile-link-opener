#!/bin/zsh
profile=$1
link=$2
open -n -a "Google Chrome" --args --profile-directory="$profile" "$link"
