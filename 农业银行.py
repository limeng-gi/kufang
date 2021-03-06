import random

print("***************************")
print("*    农业银行账户管理系统    *")
print("***************************")
print("*          1、开户         *")
print("*          2、存钱         *")
print("*          3、取钱         *")
print("*          4、转账         *")
print("*          5、查询         *")
print("*          6、再见         *")
print("***************************")
dict = {}
bank_name = "工商银行"


def dict_bank(number, username, password, country, city, street, door):
    if username in dict:
        return 2
    elif len(dict) > 100:
        return 3
    else:
        dict[username] = {
            "number": number,
            "password": password,
            "country": country,
            "city": city,
            "street": street,
            "door": door,
            "moeny": 0,
            "bank_name": bank_name
        }
    return 1


def useradd():
    number = random.randint(10000000, 88888888)
    username = input("请输入用户名：")
    password = input("请输入用户密码：")
    print("以下是详细信息：")
    country = input("\t请输入你的国家：")
    city = input("\t请输入你的省份:")
    street = input("\t请输入你的街道:")
    door = input("\t请输入你的门牌号：")
    add = dict_bank(number, username, password, country, city, street, door)
    if add == 2:
        print("该用户已存在，请重新输入")
    elif add == 3:
        print("数据库已满，不可以再添加")
    elif add == 1:
        print("以下是开户输入的详细信息：")
        info = '''
               ------个人信息------
               number：%s
               username:%s
               password:*****
               country:%s
               city:%s
               street:%s
               moeny:%s
               door:%s
               bank_name:%s
            '''
        print(info % (number, username, country, city, street, dict[username]["moeny"], door, bank_name))


def cuanqian():
    usename1 = input("请输入用户名：")
    moeny = int(input("输入存款的金额："))
    if usename1 in dict:
        dict[usename1]["moeny"] = dict[usename1]["moeny"] + moeny
    else:
        print(False)


def quqian():
    username2 = input("请输入用户信息：")
    if username2 in dict:
        word = input("请输入密码：")
        if dict[username2]["password"] == word:
            moeny1 = int(input("要取出的钱："))
            if dict[username2]["moeny"] >= moeny1:
                dict[username2]["moeny"] = dict[username2]["moeny"] - moeny1
                return 0
            else:
                return 3
        else:
            print("密码输入错误")
    else:
        return 1


def zhuanzhang():
    zc = input("请输入要转出的用户名：")
    zr = input("请输入要转入的用户名：")
    if zc and zr in dict:
        zcpassword = input("请输入转出账户的密码：")
        if zcpassword == dict[zc]["password"]:
            money3 = int(input("要转移的金额："))
            if dict[zc]["moeny"] >= money3:
                dict[zc]["moeny"] = dict[zc]["moeny"] - money3
                dict[zr]["moeny"] = dict[zr]["moeny"] + money3
            else:
                print("代号3，金额不够")
        else:
            print("代号2，密码错误")
    else:
        print("代号1，错误")


def chaxun():
    username5 = input("请输入用户名：")

    if username5 in dict:
        password5 = input("请输入密码：")
        if password5 == dict[username5]["password"]:
            info = '''
                --------个人信息--------
                当前账号：%s
                密码：%s


            '''
            print(info % (username5, password5))

        else:
            print("输入的密码不正确，请重新输入！")
    else:
        print("该用户不存在！！！！！！")


while True:
    index = int(input("请输入要进行的操作的序号："))
    if index == 1:
        print("开户")
        useradd()
        print(dict)
    elif index == 2:
        print("存钱")
        cuanqian()
        print(dict)
    elif index == 3:
        print("取钱")
        quqian()
        print(dict)
    elif index == 4:
        print("转账")
        zhuanzhang()
        print(dict)
    elif index == 5:
        print("查询")
        chaxun()
        print(dict)






