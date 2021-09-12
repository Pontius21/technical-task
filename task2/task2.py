import sys
with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'r') as b:
     p = f.read().split()
     c = b.read().split()
from math import sqrt
for i in range(0,len(c),2):
    hyp = sqrt((float(p[0])-float(c[i]))**2+(float(c[i+1])-float(p[1]))**2)
    if float(p[2]) == hyp:
        print(0)
    elif float(p[2]) > hyp:
        print(1)
    else:
        print(2)
