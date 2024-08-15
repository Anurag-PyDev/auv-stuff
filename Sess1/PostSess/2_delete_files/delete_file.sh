#!/bin/bash

echo "Enter the relative file path: "
read fname

if [ -e $fname ];then
rm -f "$fname"
else
echo "not found"
fi
