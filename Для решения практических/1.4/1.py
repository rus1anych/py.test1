from bs4 import BeautifulSoup
from urllib.request import urlopen
resp = urlopen('https://stepik.org/media/attachments/lesson/209723/4.html') # скачиваем файл
html = resp.read().decode('utf8') # считываем содержимое
soup = BeautifulSoup(html, 'html.parser') 


numbers = []
for td in soup.find_all('td'):
    result = int(td.getText()) 
    numbers.append(result)
    # sum = sum + result
#     result.append(int(float(td.getText())))
print(sum(numbers))