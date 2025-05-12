
seats = [False] * 20

while True:
    for i in range(20):
        if seats[i]:
            print(f"{i+1}[o]", end=' ')
        else:
            print(f"{i+1}[ ]", end=' ')
    print()


    num = int(input())


    if num == 0:
        print("프로그램을 종료합니다.")
        break


    elif num < 1 or num > 20:
        print("올바르지 않은 좌석번호입니다")
        continue


    if seats[num - 1]:
        print(f"좌석 {num} 은 이미 예약되어 있습니다")
    else:
        seats[num - 1] = True
        print(f"좌석 {num} 을 예약하였습니다")
