#!/usr/bin/env bash
count=0
while true; do
    count=$((count + 1))
    ./target.sh > out.txt 2> err.txt
    if [ $? -ne 0 ]; then
        echo "脚本运行失败！一共执行了 $count 次"
        echo "====标准输出 out.txt===="
        cat out.txt
        echo "====标准错误 err.txt===="
        cat err.txt
        break
    fi
done
