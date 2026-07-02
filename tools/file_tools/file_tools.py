# =============== 引入函数组 ===============

import os
import shutil

# =============== 菜单 ===============
def show_menu():
    print("1.进入一键修改所有文件名")
    print("2.进入批量修改相同后缀文件名")
    print("3.进入一键恢复修改后的文件名原名：每次只能恢复新命名的上次原名，如需恢复到最初名，可以多次执行该程序")
    print("4.进入恢复相同后缀的文件名原名")
    print("5.进入查询文件夹列表的文件")
    print("6.进入自动整理文件")
    print("7.返回上一级菜单")

# =============== 备份函数 ===============

def load_backup():
    try:
        with open("./backup.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                data = line.strip().split("|")
                if len(data) == 2:
                    new_name = data[0]
                    old_name = data[1]
                    save_old_name[new_name] = old_name
    except FileNotFoundError:
        pass


def save_backup():
    with open("./backup.txt", "w", encoding="utf-8") as f:
        for new_name in save_old_name:
            old_name = save_old_name[new_name]
            f.write(f"{new_name}|{old_name}\n")


# =============== 功能函数 ===============

def save_name(old_name,new_name):
    save_old_name[new_name] = old_name

def recover_name(folder_path,new_name):
    if new_name in save_old_name:
        old_name = save_old_name[new_name]
        new_name_path = os.path.join(folder_path,new_name)
        old_path = os.path.join(folder_path,old_name)
        os.rename(new_name_path, old_path)
        del save_old_name[new_name]
        save_backup()

def rename_all_files():
    folder_path = input("输入文件所在的文件夹路径")
    prefix_name = input("输入要修改文件所加的前缀")
    number = 1 #这里把遍历也写进函数是因为这个number如果不用c语言的指针或常变量的形式好像不能保证number的保持可加性
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            old_body_name, suffix = os.path.splitext(file)
            new_name = f"{prefix_name}_{number:03}_{old_body_name}{suffix}"
            number+=1
            new_path = os.path.join(folder_path, new_name)
            if os.path.exists(new_path):
                print("与已知文件重名,停止此次命名")
            else:
                os.rename(file_path, new_path)
                save_name(file, new_name)
                save_backup()
    print("一键命名已完成")

def rename_files_by_suffix():
    folder_path = input("输入文件所在的文件夹路径")
    want_change_suffix = "." + input("输入要修改的文件的后缀类型名(不需要加.)")
    prefix_name = input("输入要修改文件所加的前缀")
    number = 1
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            old_body_name, suffix = os.path.splitext(file)
            if suffix == want_change_suffix:
                new_name = f"{prefix_name}_{number:03}_{old_body_name}{suffix}"
                number += 1
                new_path = os.path.join(folder_path, new_name)
                if os.path.exists(new_path):
                    print("与已知文件重名,停止此次命名")
                else:
                    os.rename(file_path, new_path)
                    save_name(file, new_name)
                    save_backup()
            else:
                pass
    print(f"批量命名{want_change_suffix}类型已完成")

def recover_all_files():
    folder_path = input("输入文件所在的文件夹路径")
    user_ensure = input("确认是否恢复所有文件原名! \nPress y to ensure")
    if user_ensure == "y":
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                recover_name(folder_path, file)
        print("已恢复所有文件原名")
    else:
        print("未执行所有文件恢复原名的操作")

def recover_files_by_suffix():
    folder_path = input("输入文件所在的文件夹路径")
    want_change_suffix = "." + input("输入要恢复的文件的后缀类型名(不需要加.)")
    user_ensure = input("确认是否恢复所选后缀文件原名! \nPress y to ensure")
    if user_ensure == "y":
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                new_name, suffix = os.path.splitext(file)
                if suffix == want_change_suffix:
                    recover_name(folder_path, file)
        print("已恢复所选后缀文件原名")
    else:
        print("未执行恢复所选后缀文件原名的操作")

def show_file_list():
    found = False
    folder_path = input("输入文件所在文件夹路径")
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            print(f"{file}")
            found = True
    if not found:
        print("文件夹中未找到文件")

def organize_files():
    folder_path = input("输入文件所在文件夹路径")
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_name, suffix = os.path.splitext(file)
            folder_name = f"{suffix[1:]}文件夹"
            folder_folder_path = os.path.join(folder_path, folder_name)
            if not os.path.exists(folder_folder_path):
                os.mkdir(folder_folder_path)
            in_folder_path = os.path.join(folder_folder_path, file)
            if os.path.exists(in_folder_path):
                print(f"发现重名文件，跳过:{file}")
            else:
                shutil.move(file_path, in_folder_path)
                print(f"{file}->{folder_name}")
    print("文件已自动归类整理")

# =============== 全局变量 ===============


save_old_name = {}

#程序启动时加载一次备份，以后一直使用内存中的数据
load_backup()

# =============== 模块入口 ===============

def file_tools_menu():

    while True:
        print("")
        show_menu()
        user_choose = input("输入数字选择功能：")

        if user_choose == "1":
            rename_all_files()

        elif user_choose == "2":
            rename_files_by_suffix()

        elif user_choose == "3":
            recover_all_files()

        elif user_choose == "4":
            recover_files_by_suffix()

        elif user_choose == "5":
            show_file_list()

        elif user_choose == "6":
            organize_files()

        elif user_choose == "7":
            save_backup()
            print("返回上一级菜单")
            break

        else:
            print("输入错误")