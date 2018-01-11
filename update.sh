#!/bin/bash

# Fedora
if [[ $(uname -r) | grep "fc" ]]; then
  yum update -y
elif [[ {$(uname -r) | grep "586"} ]]; then
  apt-get update && apt-get dist-upgrade -y
fi
