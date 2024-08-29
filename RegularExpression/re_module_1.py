import re

# # findall 匹配所有字符串，符合正则的内容
# lst = re.findall(r"\d+", "我的电话号码是:10086, 我朋友的电话号码是:10011")
# print(lst)

# # finditer：匹配字符串中的所有内容[返回的是迭代器], 从迭代器中拿到的东西需要.group()
# it = re.finditer(r"\d+", "我的电话号码是:10086, 我朋友的电话号码是:10011")
# for i in it:
#     print(i.group())


# # search 拿到的是match对象，拿数据需要.group, search 只匹配第一个
# s = re.search(r"\d+", "我的电话号码是:10086, 我朋友的电话号码是:10011")
# print(s.group())

# # match 从头开始匹配
# s = re.match(r"\d+", "10086, 我朋友的电话号码是:10011")
# print(s.group())

# # 预加载正则表达式
# obj = re.compile(r"\d+")

# ret = obj.finditer("我的电话号码是:10086, 我朋友的电话号码是:10011")
# for it in ret:
#     print(it.group())


s = """
<div class='jay'><span id = '1'>张三</span></div>
<div class='ja'><span id = '2'>李四</span></div>
<div class='jb'><span id = '3'>王五</span></div>
<div class='jc'><span id = '4'>赵六</span></div>
<div class='jd'><span id = '5'>刘七</span></div>
"""

obj = re.compile(r"<div class='.*?>'<span id = '(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S) # re.S 匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group("id"))
    print(it.group("name"))
