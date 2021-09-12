import sys
import json
with open(sys.argv[1], 'r') as j1, open(sys.argv[2], 'r') as j2:
     t = json.load(j1)
     v = json.load(j2)
def f(a,b,c):
    for i in b['values']:
        for j in a[c]:
            if j['id']==i['id']:
                j['value']=i['value']
            if 'values' in j:
                f(j,b,'values')
f(t,v,'tests')
with open('report.json','w') as j3:
     json.dump( t, j3, indent=2)
