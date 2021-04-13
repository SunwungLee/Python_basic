'''

13.April.2021
Turtle 을 사용한 For문 실습

'''

import turtle
import random as rdm
t = turtle.Turtle()
t.shape("turtle")

'''
# triangle
for i in range(3):
    t.forward(100)
    t.left(360 / 3) # degree

# move turtle to 200 points forward
t.penup()
t.goto(200,0) # 해당 좌표로 펜을 옮김.
t.pendown()

# rectangular
for i in range(4):
    t.forward(100)
    t.left(360 / 4)
'''
'''
# 입력 받은 n 각형 그리기
n = turtle.textinput("", "n을 입력: ")
n = int(n)

for i in range(n):
    t.forward(100)
    t.left(360/n)
'''
'''
# random 선그리기
for i in range(30):
    length = rdm.randint(1,100)
    t.forward(length)
    angle = rdm.randint(-180,180)
    t.right(angle)
'''
for cnt in range(9):
    t.circle(100)
    t.left(360/9)
        
