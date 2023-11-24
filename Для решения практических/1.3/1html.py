from bs4 import BeautifulSoup
 
with open("D:\\Тест прогсы\\py.test1\\py.test1-1\\Для решения практических\\1.3\\index.html", "r") as f:
    
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
 
    print(soup.h2)
    print(soup.head)
    print(soup.li)
    