# 입력값 int 로
total = 0
while True:
    a = int(input())

    total += a
    if a > 0:
        print(f'입금: {a} 잔액: {total}')

    elif a < 0:

        withdraw = -a
        if total < 0:
            print("잔액이 부족합니다")
            continue
        print(f'출금: {withdraw} 잔액: {total}')

    elif a == 0:
        break
