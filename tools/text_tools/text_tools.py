# =============== 引入函数组 ===============
import os


# =============== 菜单 ===============
def show_menu():
    print("1.查看txt内容")
    print("2.统计字数和行数")
    print("3.统计关键词出现次数")
    print("4.合并txt文件")
    print("5.返回上一级菜单")

# =============== 功能函数 ===============
def view_text_content_menu():
    text_path = input("输入所查询文件路径：")

    try:
        with open(text_path,"r",encoding="utf-8") as f:
            text_content = f.read()
            print(text_content)
    except FileNotFoundError:
        print("没有找到文件，路径可能输入错误")

def count_text_content(text_path):
        with open(text_path,"r",encoding="utf-8") as f:
            text_content = f.read()
            char_count = len(text_content.replace("\n","").replace("\r",""))
            line_count = len(text_content.splitlines())
            return char_count,line_count


def count_text_content_menu():
    text_path = input("输入所查询文件路径：")
    try:
        char_count,line_count = count_text_content(text_path)
        print(f"字符数：{char_count}")
        print(f"行数：{line_count}")

    except FileNotFoundError:
        print("没有找到文件，路径可能输入错误")

def count_text_keywords(text_path,keywords):
    with open(text_path,"r",encoding="utf-8") as f:
        text_content = f.read()
        #keywords_count = len(text_content.split(keywords))
        keywords_count = text_content.count(keywords)
        return keywords_count

def count_text_keywords_menu():
    text_path = input("输入所查询文件路径：")
    keywords = input("输入所查询关键字：")
    try:
        keywords_count = count_text_keywords(text_path,keywords)
        print(f"关键词{keywords}出现了{keywords_count}次")

    except FileNotFoundError:
        print("没有找到文件，路径可能输入错误")

def merge_txt_files(merge_folder_path):
    merge_content = ""
    for file in sorted(os.listdir(merge_folder_path)):
        # 换排序方式后遍历
        file_path = os.path.join(merge_folder_path,file)
        if os.path.isfile(file_path) and file.endswith(".txt") and file != "merge.txt":
            with open(file_path,"r",encoding="utf-8") as f:
                text_content = f.read()
                merge_content += file + "\n" + text_content + "\n"
    return merge_content

def merge_txt_files_menu():
    print("将所需合并的文件放到同一个文件夹中")
    print("注意，如果有多个文件名前有数字，需要按照相同位数来命名，在不足位数的前面加0补齐，否则可能发生排序错误")
    merge_folder_path = input("输入文件夹路径")
    try:
        merge_content = merge_txt_files(merge_folder_path)
        merge_path = os.path.join(merge_folder_path,"merge.txt")
        with open(merge_path,"w",encoding="utf-8") as f:
            f.write(merge_content)
    except FileNotFoundError:
        print("没有找到文件，文件夹里可能没有文件，或者路径可能输入错误")




# =============== 模块入口 ===============

def text_tools_menu():
    while True:
        print("")
        show_menu()
        user_choose = input("输入数字选择功能：")
        if user_choose == "1":
            view_text_content_menu()
        elif user_choose == "2":
            count_text_content_menu()
        elif user_choose == "3":
            count_text_keywords_menu()
        elif user_choose == "4":
            merge_txt_files_menu()
        elif user_choose == "5":
            print("返回上一级菜单")
            break
        else:
            print("输入错误")



