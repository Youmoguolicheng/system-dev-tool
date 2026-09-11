# 简易命令行计算器
def calculator():
    print("=== 简易命令行计算器 ===")

    # 输入第一个数字（带错误校验）
    while True:
        try:
            num1 = float(input("请输入第一个数字: "))
            break
        except ValueError:
            print("输入错误，请输入有效的数字。")

    # 输入第二个数字（带错误校验）
    while True:
        try:
            num2 = float(input("请输入第二个数字: "))
            break
        except ValueError:
            print("输入错误，请输入有效的数字。")

    # 选择运算类型
    print("\n请选择运算类型：")
    print("1 - 加法 (+)")
    print("2 - 减法 (-)")
    print("3 - 乘法 (*)")
    print("4 - 除法 (/)")
    
    while True:
        op = input("请输入选项（1/2/3/4）或运算符（+-*/）: ").strip()
        
        if op in ('1', '+'):
            result = num1 + num2
            op_symbol = '+'
            break
        elif op in ('2', '-'):
            result = num1 - num2
            op_symbol = '-'
            break
        elif op in ('3', '*'):
            result = num1 * num2
            op_symbol = '*'
            break
        elif op in ('4', '/'):
            if num2 == 0:
                print("错误：除数不能为零，请重新选择运算。")
                continue
            result = num1 / num2
            op_symbol = '/'
            break
        else:
            print("输入无效，请输入 1/2/3/4 或 +-*/ 中的一个。")

    # 输出计算结果
    print(f"\n计算结果：{num1} {op_symbol} {num2} = {result}")

if __name__ == "__main__":
    calculator()

