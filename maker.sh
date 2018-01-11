#!/bin/bash

read -p "1) Webkit Dir; 2) ; 3 for service: " -n1 INPUT

if [[ $INPUT == 1 ]]; then
  service httpd start; service mysqld start
elif [[ $INPUT == 2 ]]; then
  service httpd stop; service mysqld stop
elif [[ $INPUT == 3 ]]; then
  service httpd status; service mysqld status
fi
