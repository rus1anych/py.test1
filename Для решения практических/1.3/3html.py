# Можно перебрать название всех тегов
from bs4 import BeautifulSoup
 
with open("D:\\Тест прогсы\\py.test1\\py.test1-1\\Для решения практических\\1.3\\index.html", "r") as f:
    
    contents = f.read()
 
    soup = BeautifulSoup(contents, 'lxml')
            
    for child in soup.recursiveChildGenerator():
        
        if child.name:
            
            print(child.name)
            