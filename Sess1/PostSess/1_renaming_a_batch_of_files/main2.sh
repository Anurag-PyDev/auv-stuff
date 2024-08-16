#!/bin/bash
#This script renames all files in working_dir to prefix with a number in front of it


echo "Enter name prefix :"
read np
count=0
for f in "working_dir"/*
do
count=$((count+1))
mv "$f" "working_dir/$np $count.txt"
done
