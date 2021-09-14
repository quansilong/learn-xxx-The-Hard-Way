#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

if [ ! -e $1 ]; then
  echo "Can't dentified."
elif [ -f $1 ]; then 
  echo "$1 is a file."
elif [ -d $1 ]; then 
  echo "$1 is a directory."
else
  echo "Can't dentified."
fi
