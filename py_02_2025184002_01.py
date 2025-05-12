import turtle

t = turtle.Turtle()
t.shape('turtle')
t.left(90)#터틀이 위로 향하게 하는 코드
t.up()

#좌표 이동 코드를 바로 밑줄에 입력해 주세요.
#t.goto(,)


def giyeok():
    t.forward(60)
    t.right(120)
    t.forward(80)
    t.left(120)


# '기'
t.right(90)
t.down()
giyeok()
'''t.forward(60)
t.right(120)
t.forward(80)
t.left(120)'''
t.up()
t.forward(50)
t.left(90)
t.down()
t.forward(70)

# 다음글자 이동
t.up()
t.left(180)
t.forward(90)
t.down()
# '해'
t.forward(60)
t.left(180)
t.forward(30)
t.right(90)
t.forward(10)
t.right(90)
t.forward(30)
t.left(180)
t.forward(60)

t.left(90)
t.up()
t.forward(50)

t.down()
t.left(90)
t.forward(10)
t.left(90)
t.forward(25)
t.left(180)
t.forward(50)

t.up()
t.left(90)
t.forward(30)
t.down()
t.circle(25)

# 다음글자 이동
t.up()
t.left(90)
t.forward(25)
t.right(90)
t.forward(35)

# 찬
t.down()
t.forward(10)
t.right(90)
t.forward(30)
t.left(180)
giyeok()
t.left(60)
t.forward(40)
t.right(110)
t.forward(40)
t.left(50)

t.up()
t.forward(10)
t.down()

t.left(90)
t.forward(70)
t.left(180)
t.forward(35)
t.left(90)
t.forward(10)

t.up()
t.right(90)
t.forward(60)
t.right(90)
t.down()

t.forward(60)
t.right(90)
t.forward(20)

turtle.exitonclick()