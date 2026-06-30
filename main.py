from tools import file_tools, text_tools


def show_main_menu():
    print("===== ToolBox V0.1 =====")
    print("1.文件工具")
    print("2.文本工具")
    print("3.退出")



while True:
    show_main_menu()
    user_choose = input("输入数字以选则功能：")

    if user_choose == "1":
        file_tools.file_tools_menu()

    elif user_choose == "2":
        text_tools.text_tools_menu()

    elif user_choose == "3":
        print("退出mian程序")
        break

    else:
        print("输入错误")