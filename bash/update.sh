#!/bin/bash

if [[ $(uname -r) | grep "fc" ]]; then # rh based distros
  yum update -y
elif [[ {$(uname -r) | grep "586"} ]]; then # deb based distros
  apt-get update && apt-get dist-upgrade -y
fi
