#!/bin/bash

echo "enter the file extension : "
read qext

for f in *.${qext}
do
echo "enter the new name for $f :"
read new
mv $f $new
done
