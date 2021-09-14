#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

USER_UID=`id -u $1`
GROUP_ID=`id -g $1`
if [ $USER_UID -eq $GROUP_ID ]; then 
  echo "good guy"
else
  echo "bad guy"
fi
