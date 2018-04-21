#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-21

for I in {1..100}; do
    let YUSHU=$I%3
    if [ $YUSHU -eq 0 ]; then
        echo " $I 可以被 3 整除。"
    fi
done
