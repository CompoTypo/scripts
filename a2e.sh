#!/bin/bash

source=$1
if [ -e "$source" ]
then
    echo $source 
    #as source -o 
    #ld
else
    echo $source
    echo "whelp"
fi