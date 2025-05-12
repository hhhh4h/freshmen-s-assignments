dist =  149597870.7
speed = 299792.458
time = dist//speed
minute = int(time // 60)
second = int(time % 60)
print(f'{minute}분 {second}초')