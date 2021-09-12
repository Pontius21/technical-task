import sys
with open(sys.argv[1], 'r') as f:
    data = f.read().split()
result=0
from math import floor
for i in data:
    result+=abs(int(i)-int(data[floor(len(data)/2)]))
print(result)
