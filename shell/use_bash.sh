#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

BASH_USER_NUMBER=$( grep "bash$" /etc/passwd | wc -l )
if [ $? -eq 0 ]; then
  echo "There are $BASH_USER_NUMBER user(s) which use(s) bash."
else
  echo "There aren't any users which use bash."
fi
