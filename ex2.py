# прога для нахождения количества совпадений (значения между тегами)
from urllib.request import urlopen
html = urlopen ("file:///C:/Users/acer/Downloads/2.html").read().decode('utf-8')
s = str(html)
ans = []
state = 0
for c in s:
    if c == '</code>':
      state = 1
    if c == '<code>':
      state = 0
    elif state == 0:
      ans.append(c)
s=''.join(ans)
print (s)