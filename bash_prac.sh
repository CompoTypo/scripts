#!/bin/sh

var="ayy and oops"

echo "${var%% *}"
echo "${var##* }"
