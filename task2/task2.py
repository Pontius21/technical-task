import sys
with open(sys.argv[1], 'r') as f, open(sys.argv[2], 'r') as b:
     p = [float(s) for s in f.read().split()]
     c = [float(s) for s in b.read().split()]
from math import sqrt
for i in range(0,len(c),2):
    hyp = sqrt((p[0]-c[i])**2+(c[i+1]-p[1])**2)
    if p[2] == hyp:
        print(0)
    elif p[2] > hyp:
        print(1)
    else:
        print(2)
