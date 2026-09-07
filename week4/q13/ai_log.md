核心提示：修改cli.py，--name仅空白字符时main以SystemExit(2)退出，约束仅改cli.py、保留argparse，测试命令 python -m src.greetlab.cli --name "   " 。
智能体改动：在 a = p.parse_args() 后新增 if not a.name.strip(): raise SystemExit(2) 。
人工验证：检查代码，argparse完全未改动，仅新增判断语句，运行测试，程序退出码为2，符合预期。
