# прога для нахождения количества совпадений
from urllib.request import urlopen
html = urlopen ("file:///C:/Users/acer/Downloads/1.html").read().decode('utf-8')
s = str(html)
print (s.count('Python'))