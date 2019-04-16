#!/bin/bash

projectName=$1

if [[ -z $projectName ]]
then
    echo "Make sure you are in the right directory and"
    echo "  enter main cpp file as first arguement"
    set -o errexit 
fi

g++ $projectName
./a.out