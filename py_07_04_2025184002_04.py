import math

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("모든 수")
        else:
            print("근이 없음")
    else:
        root = -c / b
        print(f"근:{root:.2f}")
else:
    d = b ** 2 - 4 * a * c

    root1 = ((-b) + d) / (2 * a)
    root2 = ((-b) - d) / (2 * a)
    if (d > 0):
        d = math.sqrt(d)
        print(f"근1:{root1:.f2}\n근2:{root2:.f2}")
    elif (d == 0):

        root = -b / (2 * a)
        print(f"중근:{root:.2f}")
    elif (d < 0):
        print("실근 없음")
