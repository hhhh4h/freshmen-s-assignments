values = [
    27, 2, 96, 39, 39, 44, 96, 64, 21, 88,
    67, 15, 88, 19, 18, 75, 91, 13, 20, 40,
    74, 69, 73, 89, 57, 52, 81, 96, 49, 94,
    77, 99, 68, 88, 95, 88, 90, 84, 48, 3,
    85, 95, 90, 59, 25, 5, 17, 15, 78, 77,
    77, 20, 83, 98, 20, 60, 97, 9, 39, 23,
    19, 72, 16, 78, 38, 43, 69, 40, 47, 64,
    67, 45, 14, 97, 64, 48, 18, 89, 54, 85,
    51, 73, 13, 51, 4, 90, 60, 93, 23, 91,
    32, 68, 69, 85, 60, 55, 98, 11, 68, 25
]

# list 를 이용한 구현

out_list = []

for v in values:
    if v not in out_list:
        out_list.append(v)

out_list.sort()
print(len(out_list), out_list)

# set 를 이용한 구현

out_set = set()#out_set(values)로도 해결 가능
for v in values:
    out_set.add(v)#set은 중복을 허용하지 않기 때문에 그냥 v를 추가해도 됨



print(len(out_set), sorted(list(out_set)))

'''values = [
    27, 2, 96, 39, 39, 44, 96, 64, 21, 88, 
    67, 15, 88, 19, 18, 75, 91, 13, 20, 40, 
    74, 69, 73, 89, 57, 52, 81, 96, 49, 94, 
    77, 99, 68, 88, 95, 88, 90, 84, 48, 3, 
    85, 95, 90, 59, 25, 5, 17, 15, 78, 77, 
    77, 20, 83, 98, 20, 60, 97, 9, 39, 23, 
    19, 72, 16, 78, 38, 43, 69, 40, 47, 64, 
    67, 45, 14, 97, 64, 48, 18, 89, 54, 85, 
    51, 73, 13, 51, 4, 90, 60, 93, 23, 91, 
    32, 68, 69, 85, 60, 55, 98, 11, 68, 25
]
#list활용
result=[]
for i in values:
    if i not in result:# values의 값이 result에 존재하지 않으면 추가
        result.append(i)

result.sort()
print(len(result),result)
#set활용
set_values = set(values) #중복 제거
set_values = list(set_values)# 중복 제거 후 개수
set_values.sort()# 오름차순 적용.이때 반환값은 없음에 주의
print(len(set_values),set_values)'''