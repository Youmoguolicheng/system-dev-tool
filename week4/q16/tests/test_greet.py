import os
import subprocess
import sys


def test_normal_name():
    """正常姓名测试：验证合法输入输出正确，退出码为0"""
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
    env = os.environ.copy()
    env["PYTHONPATH"] = src_path
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "Alice"],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )
    assert result.returncode == 0
    assert "Hello, Alice!" in result.stdout


def test_blank_name():
    """空白姓名测试：验证纯空白输入正确返回退出码2"""
    src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
    env = os.environ.copy()
    env["PYTHONPATH"] = src_path
    result = subprocess.run(
        [sys.executable, "-m", "greetlab.cli", "--name", "   "],
        capture_output=True,
        text=True,
        check=False,
        env=env,
    )
    assert result.returncode == 2
