# 生成测试报告
from HTMLTestRunner import HTMLTestRunner
import zmail
# from HTMLTestRunner import  HTMLTestRunner
import unittest
# import  unittest
# # 加载所有测试用例
# tests = unittest.defaultTestLoader.discover(r"D:\python自动化测试\python\python1\day13【单元测试】\代码\day13",pattern="Test*.py")
tests=unittest.defaultTestLoader.discover(r"D:\python自动化测试\python\python1\day13【单元测试】\代码\day13",pattern="Test*.py")
#
# # 运行器来执行用例，并生成测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    title="计算器的测试报告",
    description="这是加法测试报告",
    verbosity=1,
    stream= open(file="计算器.html",mode="w+",encoding="utf-8")
)
# runner = HTMLTestRunner.HTMLTestRunner(
#     title = "计算器的测试报告",

#     description="这是加法测试报告",
#     verbosity=1,
#     stream= open(file="计算器.html",mode="w+",encoding="utf-8")
# )
#
# # 3.运行
# runner.run(tests)
runner.run(tests)



# 读取html里面的内容
file = open("计算器.html","r",encoding="utf-8")
msg = file.read()

# 邮件内容
msg_content = {
    "subject":"李孟的测试报告",
    "content_text": msg,
    "attachments": "D:\python自动化测试\python\python1\day13【单元测试】\代码\day13\计算器.html"
}

# 收件人
receivers = ["2431320433@qq.com"]

# 发件人
sender = {"username":"481132246@qq.com","password":"oqkkfavwnciebhai"}

# 发送邮件
server = zmail.server(sender['username'],sender['password'])  #登录邮箱
server.send_mail(receivers,msg_content)

print("邮件发送成功")






# 4.邮件发送代码  任务1：使用代码发送邮件，并把测试报告当成附件发送给我。
# 温馨：用户名，密码：smtp授权码








