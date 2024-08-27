import requests

#加入query字典，更加灵活
query = input("请输入一个你喜欢的明星： ")

url = f'https://cn.bing.com/search?q={query}'

# 加入headers 伪装的更像浏览器
headers = {
    "User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
}


#地址栏里的一般都是get方式
resp = requests.get(url, headers = headers)

print(resp)
print(resp.text)    #拿到页面源代码