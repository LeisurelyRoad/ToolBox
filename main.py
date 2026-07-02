from tools.file_tools import file_tools
from tools.text_tools import text_tools
from tools.file_analyzer import file_analyzer
from tools.duplicate_check import duplicate_check
def show_main_menu():
    print("===== ToolBox V0.1 =====")
    print("1.文件工具")
    print("2.文本工具")
    print("3.文件分析工具")
    print("4.重复文件检查工具")
    print("5.退出主程序")



while True:
    print("")
    show_main_menu()
    user_choose = input("输入数字以选则功能：")

    if user_choose == "1":
        file_tools.file_tools_menu()

    elif user_choose == "2":
        text_tools.text_tools_menu()

    elif user_choose == "3":
        file_analyzer.file_analyzer_menu()

    elif user_choose == "4":

    elif user_choose == "5":
        print("退出主程序")
        break

    else:
        print("输入错误")