ymd = 20060326
y = int(ymd/10000)

m = (ymd//100)-200600
d = ymd%100
print(f'{y:04d} 년 {m:02d}월 {d:02d}일')
