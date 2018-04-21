#!/bin/bash
# Auther: LiuGaoyong
# Date:   2018-04-21

let SUM_QISHU=0
let SUM_OUSHU=0
for I in {1..100}; do
    let YUSHU=I%2
    if [ $YUSHU -eq 0 ]; then
        let SUM_OUSHU=$SUM_OUSHU+$I
    else
        let SUM_QISHU=$SUM_QISHU+$I
    fi
done
echo "1-100的奇数和为$SUM_QISHU，偶数和为$SUM_OUSHU"
