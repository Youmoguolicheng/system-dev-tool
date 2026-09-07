## Issue
环境：Windows
复现命令：`sdt-greet --name "    "`
实际结果：程序输出 `Hello,    !`，进程退出码为0。
期望结果：当--name仅传入空白字符，程序以退出码2退出，不输出问候。

## 提交信息
标题：Add validation for whitespace‑only name argument
正文：
当--name参数仅为空白字符时，程序正常返回退出码0，不符合接口约定。
增加strip()空白校验，空白输入抛出SystemExit(2)。

## 评审意见
> Blocking
行为：传入仅含空白的--name，工具正常输出问候，返回码0。
风险：外部调用脚本无法识别非法空白输入，会造成上层逻辑出错。
建议动作：在cli.py参数解析完成后增加校验，空白输入抛出SystemExit(2)。
