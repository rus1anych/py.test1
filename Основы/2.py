X = int(input())
H = int(input())
M = int(input())
H = H*60
print ((X+H+M)//60)
print ((X+M)%60)