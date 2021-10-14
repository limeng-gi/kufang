#1、请循环遍历出所有的key
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# for i in dict:
#     print(i)
#2、请循环遍历出所有的value
# for i,a in dict.items():
#     print(a)
# 3、请在字典中增加一个键值对,"k4":"v4"
# dict["k4"]="v4"
# print(dict)

# dict={}
# dict["苹果"]=32.8
# dict["香蕉"]=22
# dict["葡萄"]=15.5
# print(dict)

#
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#
#     }
# }
# moeny1=info["小明"]["fruits"]["苹果"]+info["小明"]['fruits']["草莓"]+info["小明"]["fruits"]["香蕉"]
# moeny2=info["小刚"]["fruits"]["葡萄"]+info["小刚"]['fruits']["橘子"]+info["小刚"]["fruits"]["樱桃"]
# print(moeny1)
# print(moeny2)

# from collections import Counter
# list=[21,3,56,9,10,3,3,3,3,3,3,3]
# def counter(list):
#     return(Counter(list))
# print(counter(list))

# str="acbdoe481132246"
# dict={}
# for i in str:
#     if i not in dict:
#         dict[i]=1
#     else:
#         dict[i]+=1
# print(dict)
# list=[
#     ["spring","summer","fall","winter"],
# ["spring","summer","fall","winter"],
# ["spring","summer","fall","winter"],
# ["spring","summer","fall","winter"]
#     ]
# for i,index in enumerate(list):
#     print(i,":",index)

# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print("{}*{}={}".format(j,i,j*i),end="\t")
#         j+=1
#     i+=1
#     print("")



