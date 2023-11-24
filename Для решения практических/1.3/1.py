from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen ("file:///D:/Тест%20прогсы/py.test1/py.test1-1/Для%20решения%20практических/1.2/1.html").read().decode('utf-8')
s = str(html)
pos = s.find('<a href=')
while pos !=-1:
    posquote = s.find('"', pos+9)
    href = s[pos+9:posquote]
    print(href)
    pos=s.find('<a href=', pos + 1)