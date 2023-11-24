
from bs4 import BeautifulSoup
 
with open("D:\\Тест прогсы\\py.test1\\py.test1-1\\Для решения практических\\1.3\\index.html", "r") as f:
    
    contents = f.read()
 
    soup = BeautifulSoup(contents, 'lxml')
    print(soup)
 
    # root = soup.html
    
    # root_childs = [e.name for e in root.children if e.name is not None]
    # print(root_childs)
    
    # children - можно вывести все дочерние теги
    # decendants - Позволяет найти всех потомков тега (дочерние элементы всех уровней) <какой нибудь тег> 