#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-15

BLANK_LINE_NUMBER=$( grep "^$" $1 | wc -l )
if [ $BLANK_LINE_NUMBER -ne 0 ]; then
  echo "There are $BLANK_LINE_NUMBER blank line(s)."
else
  echo "There aren't any blank lines."
fi
