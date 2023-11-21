#можно юзать вроде но как то криво работало
#a,b=(int(i) for i in input().split())
#\
#a,b=input().split()
#a=int(a)
#b=int(b)
'''sddgsfgsdg
bvbffdgd
fgdfgdfgf'''

a,b=(int(i) for i in input().split())
s=0
count=0
while a%3!=0:
    a+=1
for i in range(a,b+1,3):
    s+=i
    count+=1
print(s/count)