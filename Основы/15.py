a,b,c,d = int(input()), int(input()), int(input()), int(input())
for i in range(c,d+1):
    print('\t',i,end='')
print()
for j in range(a,b+1):
    print(j,end='\t')
    for p in range(c,d+1):
        print(j*p, end='\t')
    print()

    