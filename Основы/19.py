# работа со строками и символами
'''
s='aTGcc' p='cc'
s.upper()  'ATGCC'
s.lower()  'ctgcc'
s.count(p) 1  сколько раз p встречается в s
s.find(p)  3 первое вхлждение (индекс) p в s
s.find('A') -1 строка 'A' не входит в s
s.replace ('c', 'C') 'aTGCC' заменяем все вхождения 'c' на 'C'

a = 'asdfg'
i=1
print(a[i])

i = 'acggtgttat'
'''

i=str(input())
s=i.replace('g','G').count('G')+i.replace('c','C').count('C')
f=len(i)
print(s/f*100)