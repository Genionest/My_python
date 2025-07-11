import subprocess

# 基本执行
result = subprocess.run(["docker", "ps", "-d"], capture_output=True, text=True)
print("输出:\n", result.stdout)
# strs = result.stdout.split('\n')
# parsed_data = []
# for line in strs:
#     # 用连续空格分割后过滤空元素,单词中间可能会有一个空格，所以用两个空格
#     # if p.strip() 代表 p.strip() 不为空
#     parts = [p.strip() for p in line.split('  ') if p.strip()]
#     # parsed_data.append(parts)
#     print(",".join(parts))
print("错误:", result.stderr)
print("返回码:", result.returncode)

# 使用 shell 执行复杂命令（慎用！有安全风险）
# subprocess.run("echo $HOME && ls | grep .py", shell=True, check=True)