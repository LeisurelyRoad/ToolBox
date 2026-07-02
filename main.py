from tools import file_tools, text_tools, file_analyzer

def show_main_menu():
    print("===== ToolBox V0.1 =====")
    print("1.文件工具")
    print("2.文本工具")
    print("3.文件分析工具")
    print("4.退出主程序")


test = {
    "1": "file_tools" }
test["2"] = "test"
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
        print("退出主程序")
        break

    else:
        print(5)
        print(f"{test}")
        print(f"{test["2"]}")
        print("输入错误")