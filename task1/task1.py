import sys
n = int(sys.argv[1])
m = int(sys.argv[2])
s=[]
for i in range(m):
	for j in range(1, n+1):
		s.append(j)
i=0
stop=0
while s[i]!=stop:
    print(s[i])
    i+=m-1
    stop=1

