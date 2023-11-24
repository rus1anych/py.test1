# читает html файл
import re
from urllib.request import urlopen

html = urlopen ("file:///D:/Тест%20прогсы/py.test1/py.test1-1/Для%20решения%20практических/1.2/1.html").read().decode('utf-8')
s = str(html)
result = re.findall('<code>(.*?)</code>', s)

# находит максимальное число вхождений

counts = {}

for item in result:
    counts[item] = counts.get(item, 0) + 1

    max_count = max(counts.values())

    top_items = [item for item, count in counts.items() if count == max_count]
print(top_items)