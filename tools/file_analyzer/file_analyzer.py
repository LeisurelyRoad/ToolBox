# =============== 引入函数组 ===============
import os


# =============== 菜单 ===============
def show_menu():
    print("1.统计文件总数")
    print("2.文件夹内指定后缀文件数量")
    print("3.统计各种文件占比")
    print("4.统计文件总大小")
    print("5.查找最大文件")
    print("6.查找指定后缀中最大文件")
    print("7.从大到小排序输出前N个文件")
    print("8.返回上一级菜单")
# =============== 统计文件名，后缀，和文件大小函数 与 输入信息函数 ===============
def get_file_info(folder_path):
    file_info = []
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_part_name , file_suffix = os.path.splitext(file)
            file_size = os.path.getsize(file_path)
            file_info.append({"name": file_part_name , "suffix": file_suffix , "size": file_size})

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
def count_total_numbers(file_info):
    return len(file_info)

def count_suffix_numbers(file_info):
    suffix_count = {}
    for file_dictionary in file_info:
        suffix = file_dictionary["suffix"]
        if suffix == "":
            suffix = "无后缀"
        suffix_count[suffix] = suffix_count.get(suffix, 0) + 1
    return suffix_count

def count_suffix_percentage(file_info):
    suffix_percentage = {}
    total_numbers = count_total_numbers(file_info)
    if total_numbers == 0:
        return suffix_percentage
    suffix_count = count_suffix_numbers(file_info)
    for suffix in suffix_count:
        percentage = suffix_count[suffix] / total_numbers * 100
        suffix_percentage[suffix] = percentage
    return suffix_percentage

def count_total_size(file_info):
    total_size = 0
    for file_dictionary in file_info:
        total_size += file_dictionary["size"]
    return total_size

def find_largest_file(file_info):
    max_file_info = file_info[0]
    for file_dictionary in file_info:
        if file_dictionary["size"] > max_file_info["size"]:
            max_file_info = file_dictionary
    return max_file_info

def find_largest_suffix_file(file_info,suffix):
    find_suffix = False
    for file_dictionary in file_info:
        if file_dictionary["suffix"] == suffix:
            max_suffix_file_info = file_dictionary
            find_suffix = True
    if find_suffix:
        for file_dictionary in file_info:
            if file_dictionary["suffix"] == suffix:
                if file_dictionary["size"] > max_suffix_file_info["size"]:
                    max_suffix_file_info = file_dictionary
        return max_suffix_file_info
    else:
        return None

def get_top_n_files(file_info,n):
    all_biggest_to_smallest = sorted(file_info, key=lambda x: x["size"],reverse=True)
    if n == 0:
        return all_biggest_to_smallest
    else:
        return all_biggest_to_smallest[:n]


# =============== 模块入口 ===============
def file_analyzer_menu():
    while True:
        print("")
        show_menu()
        user_choose = input("输入数字进入对应功能")

        if user_choose == "1":
            file_info = input_file_info()
            if file_info is None:
                continue
            total_files = count_total_numbers(file_info)
            print(f"文件夹总数量：{total_files}")

        elif user_choose == "2":
            file_info = input_file_info()
            if file_info is None :
                continue
            suffix_count = count_suffix_numbers(file_info)
            for suffix in suffix_count:
                print(f"后缀为{suffix}的文件有{suffix_count[suffix]}个")

        elif user_choose == "3":
            file_info = input_file_info()
            if file_info is None:
                continue
            suffix_percentage = count_suffix_percentage(file_info)
            for suffix in suffix_percentage:
                print(f"后缀为{suffix}的文件占所有文件的占比为{suffix_percentage[suffix]:.2f}%")
            # if not suffix_percentage:
            #     print("文件夹中没有可分析的文件，可能该文件夹为空，或者输入了错误的文件夹路径")

        elif user_choose == "4":
            file_info = input_file_info()
            if file_info is None:
                continue
            total_size = count_total_size(file_info)
            print(f"文件的总大小是{total_size}")

        elif user_choose == "5":
            file_info = input_file_info()
            if file_info is None:
                continue
            max_file_info = find_largest_file(file_info)
            print(f"最大文件{max_file_info['name']}的占用是{max_file_info['size']}")
            #注意到这里只有'有自动填充成俩个的功能，在{}里的字典的字符串key可以用'来引用吗

        elif user_choose == "6":
            file_info = input_file_info()
            if file_info is None:
                continue
            suffix = input("输入所选文件的后缀")
            max_suffix_file_info = find_largest_suffix_file(file_info,suffix)
            if not max_suffix_file_info:
                print(f"文件夹内没有后缀为{suffix}的文件")
                continue
            print(f"在后缀为{suffix}的文件中,文件{max_suffix_file_info['name']}的占用最大，为{max_suffix_file_info['size']}")

        elif user_choose == "7":
            file_info = input_file_info()
            if file_info is None:
                continue
            try:
                n = int(input("输入想查的前n个文件，如果输入0，则将所有文件按从大到小排序呈现出来"))
                if n < 0:
                    print("输入的数字应为大于等于0的整数")
                    continue
                top_n_files_info = get_top_n_files(file_info,n)
                for i , x in enumerate(top_n_files_info,start=1):
                    print(f"{i}.{x['name']}{x['suffix']}:{x['size']}字节")
            except ValueError:
                print("输入的数字应为大于等于0的整数")

        elif user_choose == "8":
            print("返回上一级菜单")
            break
        else:
            print("输入错误")