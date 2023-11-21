a=int(input())
b=int(input())
c=int(input())
d=int(input())

print('\t', *range(c, d+1), sep='\t')
for i in range(a,b+1):
    print(i, *range(i*c,(i*d)+1, i), sep='\t')