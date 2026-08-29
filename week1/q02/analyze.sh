# 脚本接收1个参数：csv文件路径
if [ $# -ne 1 ]
then
    echo "使用方式: $0 输入csv文件" >&2
    exit 1
fi

infile="$1"

# 判断普通文件是否存在
if [ ! -f "$infile" ]
then
    echo "错误：文件 $infile 不存在" >&2
    exit 2
fi

echo "HTTP 5xx最多的前2个path:"
awk -F ',' 'NR>1 && $4 ~ /^5[0-9][0-9]$/ {count[$3] = count[$3] + 1}
END {
    for(p in count) {
        print count[p], p
    }
}' "$infile" | sort -k1,1nr -k2,2 | head -2

echo ""
echo "latency_ms平均值:"
awk -F ',' 'NR>1 {total = total + $5; num = num + 1}
END {
    printf "%.2f\n", total / num
}' "$infile"
