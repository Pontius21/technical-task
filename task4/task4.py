import sys
with open(sys.argv[1], 'r') as f:
    data = [int(s) for s in f.read().split()]
data.sort()
result=0
from math import floor
for i in data:
    result+=abs(i-data[floor(len(data)/2)])
print(result)
