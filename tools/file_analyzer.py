# =============== 引入函数组 ===============
import os


# =============== 菜单 ===============
def show_menu():
    print("1.统计文件总数")
    print("2.统计文件后缀数量")
    print("3.统计各种文件占比")
    print("4.统计文件总大小")
    print("5.查找最大文件")
    print("6.查找某种后缀最大的文件")
    print("7.从大到小排序输出前N个文件")
    print("8.返回上一级菜单")
# =============== 统计文件名，后缀，和文件大小函数 ===============
def get_file_info(folder_path):
    file_info = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_part_name , file_suffix = os.path.splitext(file)
            file_size = os.path.getsize(file_path)
            file_info.append({"name": file_part_name , "suffix": file_suffix , "size": file_size})

    return file_info

# =============== 功能函数 ===============
def count_total_numbers(file_info):
    return len(file_info)

def count_suffix_numbers(file_info):
    suffix_count = {}
    for file_dictionary in file_info:
        suffix = file_dictionary["suffix"]
        if suffix == "":
            suffix = "无后缀"




# =============== 模块入口 ===============
def file_analyzer_menu():
    while True:
        print("")
        show_menu()
        user_choose = input("输入数字进入对应功能")
        if user_choose == "1":
            folder_path = input("输入文件夹路径")
            file_info = get_file_info(folder_path)
            total_files = count_total_numbers(file_info)
            print(f"文件夹总数量：{total_files}")

        elif user_choose == "2":
            print("文件分析工具功能开发中")

        elif user_choose == "3":
            print("文件分析工具功能开发中")

        elif user_choose == "4":
            print("文件分析工具功能开发中")

        elif user_choose == "5":
            print("文件分析工具功能开发中")

        elif user_choose == "6":
            print("文件分析工具功能开发中")

        elif user_choose == "7":
            print("文件分析工具功能开发中")

        elif user_choose == "8":
            print("返回上一级菜单")
            break
        else:
            print("输入错误")