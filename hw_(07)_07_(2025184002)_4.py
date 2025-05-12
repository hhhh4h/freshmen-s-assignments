edges = [

    (0, 1, 668), (0, 2, 312), (0, 4, 128), (1, 2, 652), (1, 3, 1206),

    (1, 5, 958), (2, 4, 902), (2, 6, 476), (2, 7, 175), (3, 5, 540),

    (3, 6, 449), (3, 7, 601), (4, 6, 430), (6, 7, 925)

]
#g = dict()
g = {k: dict() for k in range(8)}
for start, end, weight in edges:
    '''if start not in g:#g안에 strat라는 키가 없으면 추가    -->딕셔너리를 추가하기 위해
        g[start]=dict()#g[start][end]를 만들기 위해서 g[start]를 먼저 생성 해야함.'''
    g[start][end]=weight
for i in range(8):
    for j in range(8):
        if i in g and j in g[i]:
            print("%5d"% g[i][j], end ="")
        else:
            print(" "*5, end="")
    print()
