import pandas as pd
import sys
from datetime import date

filename = sys.argv[1]
data = pd.read_csv(filename, encoding="big5")

r,c = data.shape

start = 84500
end = 134500


def inS(t):
    if t>=start and t<=end:
        return True
    return False

d = data['成交日期'][0]
year = d//10000
month = d % 10000 //100
day = d%100
w = date(year, month, 1).weekday()
 
x = (2+7-w)%7
m = month % 12 + 1 if day>(14 + x) else month

s = 10000000000
e = -1
o = 0
c = 0
h = -1
l = 10000000000

for i in range(r):
    if  data['商品代號'][i].replace(" ", "") != 'TX' \
        or not inS(data['成交時間'][i]) \
        or len(data['到期月份(週別)'][i].replace(" ",""))>6 \
        or int(data['到期月份(週別)'][i].replace(" ","")[4:6]) != m:
        continue
    if data['成交時間'][i] < s:
        s = data['成交時間'][i]
        o = data['成交價格'][i]
    if data['成交時間'][i] >= e:
        e = data['成交時間'][i]
        c = data['成交價格'][i]
    if data['成交價格'][i] < l:
        l = data['成交價格'][i]
    if data['成交價格'][i] > h:
        h = data['成交價格'][i]


print(int(o), end=' ')
print(int(h), end=' ')
print(int(l), end=' ')
print(int(c))
