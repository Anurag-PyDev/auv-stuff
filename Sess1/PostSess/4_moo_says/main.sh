#!bin/bash

echo "What does the cow say... "
read cla
if [ -z $cla ];then
cowsay fortune
else
cowsay $cla
fi
