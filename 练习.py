# dict={ "曹操":56,"男":"106","IBM": 500 ,"曹贼":"ll","擦擦":"kl","拉拉":
#     {"ll":"oo","天坛":600,"哈哈":"京哈","匹配":
#             {"atm":1520,"FF":"aa","dn":
#                 {"pb":6000}}}}
# print(dict["IBM"]+dict["拉拉"]["天坛"]+dict["拉拉"]["匹配"]["atm"]+dict["拉拉"]["匹配"]["dn"]["pb"])
# dict["ou"]="da"
# print(dict)

# dict1={}
# print(dict)
# dict.popitem()
# print(dict.popitem())
# num=input("请输入两个内容：")
# for i ,a in zip(range(1,len(num)+1),num):
#     dict1[i]=a
# print(dict1)

# names = {
#     "曹操":56,"男":"106","IBM": 500 ,"关羽":
# {"大乔":19,"女":"230","微软": 501 ,"60":
#     {"小乔": 19, "女": "210", "Oracle": 600, "65":
# { "许褚": 45, "男": "230", "Tencent": 700 }}}}
# dict={}
# sum=names["IBM"]+names["关羽"]["微软"]+names["关羽"]["60"]["Oracle"]+names["关羽"]["60"]["65"]["Tencent"]
# nl=names["曹操"]+names["关羽"]["大乔"]+names["关羽"]["60"]["小乔"]+names["关羽"]["60"]["65"]["许褚"]
# #平均薪资
# print(sum,sum/4)
# #平均年龄
# print(nl,nl/4)

# dict["姓名"]="45"
# dict["性别"]="男"
# dict["编号"]="2000"
# dict["任职公司"]="alibaba"
# dict["薪资"]="9999"
# dict["部门编号"]="66"
# print(dict)
#添加数据
names = [
    ["曹操","56","男","106","IBM", 500 ,"50"],
    ["大乔","19","女","230","微软", 501 ,"60"],
    ["小乔", "19", "女", "210", "Oracle", 600, "60"],
    ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
]
# names.append(["刘备","45","男","220","alibaba",500,"30"])
# print(names)
# #男女个数
# a=0
# b=0
# for i in range(len(names)):
#      if names[i][2]=="男":
#          a+=1
#      else:
#          b+=1
# print("男生的人数为{},女生的人数为{}".format(a,b))
#每个部门的人数
# bumenlist0 = []
# bumenlist1 = []
# for j in range(5):
#     if names[j][6] not in bumenlist0:
#         bumenlist0.append(names[j][6])
# print(bumenlist0)
# for i in range(4):
#     for j in range(5):
#         count3 = 0
#         if bumenlist0[i] == names[j][6]:
#             count3 = count3 + 1
#             bumenlist1.append(count3)
# print(bumenlist1)
#
# list=[]
# for a in range(5):
#     if names[a][6] not in list:
#         list.append(names[a][6])
# print(list)
#每个部门的人数
# a=0
# b=0
# c=0
# for j in range(len(names)):
#     if names[j][6]=="60":
#         a+=1
#     elif names[j][6]=="50":
#         b+=1
#     else:
#         c+=1
# print("人数分别为{}{}{}".format(a,b,c))

# num=int(input("请输入一个数："))
# while num != 0:
#     print(num % 10)
#     num = num // 10

numbers=[1,6,4,8,7,9,2,31,20,3,5,4,6,71]
for i in range(len(numbers)-1):
    for j in range(len(numbers)-1-i):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print(numbers)




























