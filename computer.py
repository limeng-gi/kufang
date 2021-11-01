class computer:
#有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
    __pingmu=""
    __price=0.0
    __cpu=0
    __neicun=0
    __daiji=0
    def setpingmu(self,pingmu):
        if pingmu<0 or pingmu>18:
            print("你输入的电脑屏幕不存在")
        else:
            self.__pingmu=pingmu
    def getpingmu(self):
        return self.__pingmu

    def setprice(self,price):
        if price < 0 or price > 2000000:
            print("没有此价格")
        else:
            self.__price=price
    def getprice(self):
        return self.__price

    def setcpu(self,cpu):
        if cpu<0 or cpu>66666:
            print("超出规格的cpu")
        else:
            self.__cpu=cpu
    def getcpu(self):
        return self.__cpu

    def setneicun(self,neicun):
        if neicun < 0 or neicun>999:
            print("你的内存华仔设计中")
        else:
            self.__neicun=neicun
    def getneicun(self):
        return self.__neicun

    def setdaiji(self,daiji):
        if daiji<0:
            print("待机时间没有0")
        else:
            self.__daiji=daiji
    def getdaiji(self):
        return self.__daiji



    def pingmu(self,size):
        print("这个电脑的屏幕大小为",self.__pingmu,size)
    def jiage(self,jiage):
        print("这个电脑的价格为：",jiage)
    def diannao(self):
        print("电脑屏幕为",self.__pingmu,
              "价格为",self.__price,
              "cpu大小为",self.__cpu,
              "内存大小为：",self.__neicun,
              "待机时长：",self.__daiji)





c=computer()
c.setpingmu(15.6)
c.setprice(999)
c.setcpu(6666)
c.setneicun(666)
c.setdaiji(9999)
c.diannao()



