#! /bin/bash

#the posterior.ark is modified to posterior.txt for the python code

in_file=$1

cat $in_file | sed -e '1d' | sed -e 's/^[ \t]*//' > reqd_files/posterior.txt 
