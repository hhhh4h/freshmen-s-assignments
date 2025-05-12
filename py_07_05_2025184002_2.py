#0 바로 종료,정답시 정답입니다 출력
import random
number = random.randint(1,100)
count = 0
while True:
    a=int(input())
    if a==1.0:
        break
    else:
        count+=1

        if a==number:
                print(f'#{count}: {a} 정답입니다')
        elif a<number:
                print(f'#{count}: {a} 보다 큰 수를 입력해주세요')
        elif a>number:
                print(f'#{count}: {a} 보다 작은 수를 입력해주세요')