#!/bin/bash

echo "Enter the height :"
read n

temp=0
for ((i=0;i<n;i++))
do
for ((j=0;j<i;j++))
do
echo -n $((temp%10))
temp=$((temp+1))
done
echo $((temp%10))
temp=$((temp+1))
done
