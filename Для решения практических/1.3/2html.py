from bs4 import BeautifulSoup

with open("D:\\Тест прогсы\\py.test1\\py.test1-1\\Для решения практических\\1.3\\index.html", "r") as f:
    
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print("HTML: {0}, name: {1}, text: {2}".format(soup.h2, 
        soup.h2.name, soup.h2.text))