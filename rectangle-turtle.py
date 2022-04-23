import sys
print(sys.version)

import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงรางเป็นเต่า

def Rectangle():
    '''ฟังชั่้นนี้เอาไว้วาดรูปสี่เหลี่ยม'''
    for i in range(4):
        tao.forward(100)
        tao.left(90)

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()


Go(200,200)
Rectangle()
