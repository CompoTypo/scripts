#!/bin/bash

source=$1
if [ -e "$source" ]
then
    echo $source 
    name = $(echo "$source" | cut -f 1 -d '.')
    echo $name
    as $source -o $name + ".o"  
    echo $name + ".o"
else
    echo "No assembly file to assemble."
    echo "FORMAT: ./asm.sh asm_file.s"
fi