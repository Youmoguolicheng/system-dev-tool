import subprocess


def test_blank_name():
    # 传入纯空白字符串
    result = subprocess.run(["sdt-greet", "--name", "  "], check=False)
    # 要求返回码等于2
    assert result.returncode == 2


if __name__ == "__main__":
    test_blank_name()
    print("测试通过")
