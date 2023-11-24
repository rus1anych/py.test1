import xlrd

wb = xlrd.open_workbook('D:\\Тест прогсы\\py.test1\\py.test1-1\\Для решения практических\\2.1\\tab.xlsx')
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])
nmin = sh.row_values(6)[2]
for rownum in range(7, 27):
    temp = sh.row_values(rownum)
    nmin = min(nmin, temp[2])
print(nmin)