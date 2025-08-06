import os
import subprocess

# 设置路径：当前脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# Git 提交信息
commit_message = "Auto update from script"

# Git 操作命令
commands = [
    "git add .",
    f'git commit -m "{commit_message}"',
    "git push"
]

print("🔁 正在上传到 GitHub...")

for cmd in commands:
    result = subprocess.run(cmd, shell=True, cwd=base_dir)
    if result.returncode != 0:
        print(f"❌ 命令执行失败：{cmd}")
        break

print("✅ 上传完成，请检查 GitHub 仓库！")
