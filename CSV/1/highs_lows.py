import csv

with open('D:\\Тест прогсы\\py.test1\\py.test1-1\\CSV\\1\\Import_User_Sample_en.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
    
    