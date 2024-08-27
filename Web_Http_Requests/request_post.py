import requests

url = 'https://fanyi.baidu.com/sug'

s = input("请输入你要翻译的英文单词: ")

dic = {
    "kw": s
}

#发送post请求，发送的参数必须放在字典中，通过data参数进行传递
resp = requests.post(url, data= dic)
print(resp.json())  #服务器返回的内容直接处理成json，也就是python的字典