# -*- coding:utf-8 -*-

# 定义一个列表，用于存储名片
cards_list = []


def prt_menu():
    print("*" * 20)
    print("   名片管理系统v0.0")
    print("*" * 20)
    print(" 1.添加名片")
    print(" 2.删除名片")
    print(" 3.修改名片")
    print(" 4.查询名片")
    print(" 5.显示所有名片")
    print(" 6.退出系统")
    print("*" * 20)


def add_new_card_info():
    name = input("请输入名字：")
    age = input("请输入年龄：")
    phone_number = input("请输入手机号：")
    people = {"name": name, "age": age, "phone_number": phone_number}
    cards_list.append(people)
    print(cards_list)


def del_card_info():
    name = input("请输入要删除的用户名称：")
    for item in cards_list:
        if item.get("name") == name:
            cards_list.remove(item)
            break


def modify_card_info():
    name = input("请输入要修改的用户的名称：")
    age = input("请输入要修改成的用户的年龄：")
    phone_number = input("请输入要修改成的用户的手机号：")

    i = 0
    while i <= len(cards_list) - 1:
        if cards_list[i].get("name") == name:
            cards_list[i]["age"] = age
            cards_list[i]["phone_number"] = phone_number
        i += 1


def inquiry_card_info():
    name = input("请输入要查寻的名字：")
    # flag = False
    # for item in cards_list:
    #     if item.get("name") == name:
    #         print("此用户名片存在")
    #         print(item)
    #         flag = True
    #         break
    # if not flag:
    #     print("无此名片")
    for item in cards_list:
        if item["name"] == name:
            print("此用户的名片存在")
            print(item)
            break
    else:
        print("无此用户的名片")


def show_all_card_info():
    for item in cards_list:
        print("姓名\t\t\t\t年龄\t手机号")
        print("%-12s\t%-2s\t%-11s\t" % (item["name"], item["age"], item["phone_number"]))


# 提示信息
prt_menu()

# 循环执行
while True:
    # 获取用户的功能请求
    num = int(input("请问您想干什么？"))

    # 根据用户的请求，来对列表进 行“增/删/改/查”
    if num == 1:
        add_new_card_info()
    elif num == 2:
        del_card_info()
    elif num == 3:
        modify_card_info()
    elif num == 4:
        inquiry_card_info()
    elif num == 5:
        show_all_card_info()
    elif num == 6:
        break
    else:
        print("输入有误，请重新输入！！！")
