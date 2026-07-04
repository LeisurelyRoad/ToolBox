# =============== 引入函数组 ===============
import os
import hashlib

# =============== 菜单 ===============
def show_menu():
    print("1.检查文件名重复文件")
    print("2.按文件大小检查疑似重复文件")
    print("3.按文件内容检查真正重复文件")
    print("4.返回上一级菜单")

# =============== 通用函数 ===============
def get_file_info(folder_path):
    file_info = [] #列表，字典
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_part_name , file_suffix = os.path.splitext(file)
            file_size = os.path.getsize(file_path)
            file_info.append({
                "name": file_part_name,
                "suffix": file_suffix,
                "size": file_size,
                "path": file_path
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
    name_group = {} #字典，列表，字典
    for file_dictionary in file_info:
        name = file_dictionary["name"]
        if name not in name_group:
            name_group[name] = []
        name_group[name].append(file_dictionary) #name_group[name]对应的是含有字典的列表
    return name_group

def find_duplicate_names(file_info):
    name_group = group_by_name(file_info) #字典，列表，字典
    duplicate_group_names = []
    for key_name in name_group:
        names_list = name_group[key_name]
        if len(names_list) > 1:
            duplicate_group_names.append(name_group[key_name])
    if not duplicate_group_names:
        return None
    else:
        return duplicate_group_names  # 返回含有列表(里面是含有字典的列表)的列表

def group_by_size(file_info):
    size_group_dictionary = {} #字典，列表，字典
    for file_dictionary in file_info:
        size = file_dictionary["size"]
        if size not in size_group_dictionary:
            size_group_dictionary[size] = []
        size_group_dictionary[size].append(file_dictionary)
    return size_group_dictionary

def find_duplicates_size(file_info):
    size_group_dictionary = group_by_size(file_info) #字典，列表，字典
    duplicate_group_size = [] #用于处理没有重复文件的情况
    for size_key in size_group_dictionary:
        size_list = size_group_dictionary[size_key]
        if len(size_list) > 1:
            duplicate_group_size.append(size_group_dictionary[size_key])
    if not duplicate_group_size:
        return None
    else:
        return duplicate_group_size

# 查找重复文件思路：
# 打开文件，判断内容函数，内容相同的为一组
# 判断内容，每个不同的内容对应数字代号，用字典自动分组处理相同代号的
# 遍历文件夹，每个文件有其对应内容，name[内容]= []，name[内容].append(文件信息)
# 先name[内容]分组，再看组里元素多余一的即为重复文件

def group_by_contents(file_info):
    contents_group = {}
    # for file_dictionary in file_info:
    #     file_path = file_dictionary["path"]
    #     with open(file_path, "r", encoding="utf-8") as f:







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
            group_names_list = find_duplicate_names(file_info)
            if not group_names_list:
                print("文件夹内没有重名文件")
                continue
            else:
                for same_group_name_in_list in group_names_list: #in_list元素是含有字典的列表，其中字典的part_name部分相同
                    print(f"有下列含有重复名{same_group_name_in_list[0]['name']}的疑似重复文件:")
                    for file_dictionary in same_group_name_in_list:
                        print(f"{file_dictionary['name']}{file_dictionary['suffix']}")

        elif user_choose == "2":
            file_info = input_file_info()
            if not file_info:
                continue
            group_size_list = find_duplicates_size(file_info) #列表，列表，字典
            if not group_size_list:
                print("文件夹内没有文件大小相等的文件")
                continue
            else:
                for group_size_in_list in group_size_list:
                    print(f"有下列文件大小均为{group_size_in_list[0]['size']}疑似重复文件：")
                    for group_size_dictionary in group_size_in_list:
                        print(f"{group_size_dictionary['name']}：文件大小为{group_size_dictionary['size']}")

        elif user_choose == "3":
            print("3.按文件内容检查真正重复")
