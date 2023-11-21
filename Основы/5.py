a = int(input())
b = int(input())
c = int(input())
if a<=b<=c:
    print(c,'\n',a,'\n',b)
elif a<=c<=b:
    print(b,'\n',a,'\n',c)
elif b<=a<=c:
    print(c,'\n',b,'\n',a)
elif b<=c<=a:
    print(a,'\n',b,'\n',c)
elif c<=a<=b:
    print(b,'\n',c,'\n',a)
elif c<=b<=a:
    print(a,'\n',c,'\n',b)