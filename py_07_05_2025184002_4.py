#루프 돌다 약수 발견시 소수 아니다 이용
#n-1보다 루트n이 더 정확함
number = []
for i in range (2,1001):
    a = True
    for d in range(2,i):
        if i%d == 0:
            a=False
            break
    if a:
        number.append(i)
for i in range(len(number)):
    if i <len(number)-1:
        print(number[i],end=', ')
    else:
        print(number[i],end='')

print(f'[총{len(number)}개]')
