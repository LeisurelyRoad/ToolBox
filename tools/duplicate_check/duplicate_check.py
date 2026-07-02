# =============== 引入函数组 ===============
import os

# =============== 菜单 ===============
def show_menu():
    print("1.检查文件名重复")
    print("2.按文件大小检查疑似重复")
    print("3.按文件内容检查真正重复")
    print("4.返回上一级菜单")

# =============== 通用函数 ===============
def get_file_info(folder_path):
    file_info = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_part_name , file_suffix = os.path.splitext(file)
            file_size = os.path.getsize(file_path)
            file_info.append({
                "name": file_part_name,
                "suffix": file_suffix,
                "size": file_size
            })

    return file_info

def input_file_info():
    folder_path = input("输入文件夹路径")
    try:
        file_info = get_file_info(folder_path)
        if not file_info:
            print("文件夹中没有可分析的文件，可能该文件夹为空，或者输入了错误的文件夹路径")
            return None
        else:
            return file_info
    except FileNotFoundError:
        print("文件夹路径不存在，可能输入了错误的文件夹路径")
        return None

# =============== 功能函数 ===============
def group_by_name(file_info):
    name_group = {}
    for file_dictionary in file_info:
        name = file_dictionary["name"]
        if name not in name_group:
            name_group[name] = []
        name_group[name].append(file_dictionary) #name_group[name]对应的是含有字典的列表
    return name_group

def find_duplicate_names(file_info):
    name_group = group_by_name(file_info)
    duplicate_group_names = []
    for key_name in name_group:
        duplicate_names_number = len(name_group[key_name])
        if duplicate_names_number > 1:
            duplicate_group_names.append(name_group[key_name])
    if not duplicate_group_names:
        return None
    else:
        return duplicate_group_names  # 返回含有列表(里面是含有字典的列表)的列表

# =============== 模块入口 ===============
def duplicate_check_menu():
    while True:
        print("")
        show_menu()
        user_choose = input("输入数字选择功能：")
        if user_choose == "1":
            file_info = input_file_info()
            if not file_info:
                continue
            duplicate_group_names = find_duplicate_names(file_info)
            if not duplicate_group_names:
                print("文件夹内没有重名文件")
                continue
            else:
                for same_group_name in duplicate_group_names: #元素是含有字典的列表，其中字典的part_name部分相同
                    print(f"含有重复名{same_group_name[0]['name']}的文件:")
                    for file_dictionary in same_group_name:
                        print(f"{file_dictionary['name']}{file_dictionary['suffix']}")