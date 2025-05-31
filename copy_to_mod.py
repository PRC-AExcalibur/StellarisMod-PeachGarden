import os
import shutil
import sys

def copy_folder(source_folder, target_folder, ignore_folder):
    # 确保目标路径存在
    os.makedirs(target_folder, exist_ok=True)

    # 遍历源文件夹
    for root, dirs, files in os.walk(source_folder):
        # 忽略指定的文件夹
        if ignore_folder in dirs:
            dirs.remove(ignore_folder)

        # 计算相对路径
        relative_path = os.path.relpath(root, source_folder)
        target_root = os.path.join(target_folder, relative_path)

        # 确保目标子目录存在
        os.makedirs(target_root, exist_ok=True)

        # 复制文件
        for file in files:
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_root, file)
            shutil.copy2(source_path, target_path)
            print(f"复制文件 {source_path} 到 {target_path}")

# 定义要复制的文件夹路径和目标路径
source_folder = os.getcwd()  # 当前工作目录
target_folder = "C:/Users/AExcalibur/Documents/Paradox Interactive/Stellaris/mod/PeachGarden"  # 默认目标路径
if len(sys.argv) == 2:
    target_folder = sys.argv[1]  # 目标路径作为命令行参数传入

# 调用函数
copy_folder(source_folder, target_folder, ".git")
print("复制完成")