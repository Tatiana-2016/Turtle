import turtle
import time
from math import sin
t = turtle.Turtle()
t.shape("turtle")
t.color("darkgreen", "yellow")
t.shapesize(1)
t.speed(10)


def main():
    x = int(input())
    t.penup()
    t.backward(300)
    draw_number(x)
    time.sleep(20)


def draw_number(number):
    c=[]
    while number>0 :
        c.append(number % 10)
        number//= 10
    for i in range(len(c)-1,-1,-1):
        draw_digit(c[i])
    t.hideturtle()


def draw_digit(z):
    """ Рисует цифры: 1 2 3 4 5 6 7 8 9 0
    """
    if z==1:
        digit_one(50)
        t.forward(20)
    elif z==2:
        digit_two(50)
        t.forward(20)
    elif z==3:
        digit_three(50)
        t.forward(20)
    elif z==4:
        digit_four(50)
        t.forward(20)
    elif z==5:
        digit_five(50)
        t.forward(20)
    elif z==6:
        digit_six(50)
        t.forward(20)
    elif z==7:
        digit_seven(50)
        t.forward(20)
    elif z==8:
        digit_eight(50)
        t.forward(20)
    elif z==9:
        digit_nine(50)
        t.forward(20)
    else  :
        digit_zero(50)
        t.forward(20)


def digit_one(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
        контракт (договорённость):
            черепаха возвращается в исходную точку
            и имеет исходную ориентацию
            перо оказывается поднятым по окончании функции
    """
    t.penup()
    t.forward(length/2)
    t.pendown()
    t.left(90)
    t.forward(length)
    t.left(90+45)
    t.forward(length*sin(45*3.141592/180))
    #обратный ход
    t.backward(length*sin(45*3.141592/180))
    t.right(90+45)
    t.backward(length)
    t.right(90)
    t.penup()

def digit_two(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки
    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [180, -135, 45, 90]
    A = [ L1,   L2, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()

def digit_three(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки

    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [ 45, 135, -135,135]
    A = [ L2,  L1,   L2, L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)

def digit_four(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки

    """
    L1 = length/2
    L2 = length
    B = [90, 180, -90, -90]
    A = [ L2, L1, L1, L1]

    t.penup()
    t.forward(L1)
    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()


def digit_five(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки

    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [ 0, 90, 90,-90,-90]
    A = [ L1,  L1,   L1, L1,L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)

def digit_six(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки

    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [ 0, 90, 90,90,180,0,-90]
    A = [ L1,  L1,   L1, L1,L1,L1,L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)


def digit_seven(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки

    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [ 90, -45, 135]
    A = [ L1,  L2, L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)

def digit_nine(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки

    """
    L1 = length/2
    L2 = (length/2)*2**0.5
    B = [ 45, 45, 90,90,90]
    A = [ L2,  L1, L1,L1,L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)

def digit_zero(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки

    """
    L1 = length/2
    L2 = length
    B = [ 0, 90, 90,90]
    A = [ L1,  L2, L1,L2]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)

def digit_eight(length):
    """ Рисует цифру с высотой length
        слева от направления черепашки

    """
    L1 = length/2
    L2 = length
    B = [ 0, 90, 90,90,90,90,90]
    A = [ L1,  L2, L1,L2,L1,L1,L1]

    t.pendown()
    for lenght, degree in zip(A, B):
        t.left(degree)
        t.forward(lenght)
    A.reverse()
    B.reverse()
    for lenght, degree in zip(A, B):
        t.backward(lenght)
        t.right(degree)
    t.penup()
    t.forward(L1)

main()
