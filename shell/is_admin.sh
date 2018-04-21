#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

USER_UID=`id -u $1`
if [ $USER_UID -eq 0 ]; then
  echo "This is administration." 
else
  echo "This is a commen user." 
fi

