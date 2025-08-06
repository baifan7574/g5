import os
import subprocess

# 强制进入 g5 项目目录（改成你当前项目路径）
project_path = r"D:\项目\g5"
os.chdir(project_path)

# ✅ 接下来就可以正常运行 git 命令了
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Auto update"])
subprocess.run(["git", "push"])
