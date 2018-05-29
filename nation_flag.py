# -*- coding: utf-8 -*-  
import math 
import turtle
import time

def draw_grid(x,y,size):
    turtle.penup()
    turtle.home()
    turtle.pendown()
    turtle.pencolor('black')
    for i in range(int(y/2/size)):
        turtle.backward(x/2)
        turtle.penup()
        turtle.goto(0, i*size + size)
        turtle.pendown()
    turtle.penup()
    turtle.home()
    turtle.left(90)
    for i in range(int(x/2/size)):
        turtle.pendown()
        turtle.forward(x/2)
        turtle.penup()
        turtle.goto(-(i*size+size),0)


def draw_square(width, height):
    turtle.setup(width=width, height=height)
    turtle.penup()
    turtle.goto(-width/2,-height/2)
    turtle.pendown()
    turtle.color('red', 'red')    
    turtle.begin_fill()
    x = width
    y = height  
    turtle.forward(x)  
    turtle.left(90)    
    turtle.forward(y)     
    turtle.left(90)    
    turtle.forward(x)     
    turtle.left(90)    
    turtle.forward(y)    
    turtle.end_fill()  
    # time.sleep(0.5)


def draw_pentagram(center_x,center_y, size, angle_temp):
    turtle.penup()
    turtle.home()
    turtle.goto(center_x, center_y)
    # print(turtle.pos())
    turtle.left(162 + angle_temp)
    turtle.forward(3*size)
    turtle.right(162)
    turtle.color('yellow','yellow')
    turtle.begin_fill()
    turtle.pendown()
    for i in range(5):
        turtle.forward(6*size*math.sin(72*math.pi/180))
        turtle.right(144)
    turtle.end_fill()  
    # time.sleep(0.5)


def draw_five_pentagram(size):
    draw_pentagram(-10*size, 5*size, size, 0)
    draw_pentagram(-5*size, 8*size, size/6, math.atan(3/5)*180/math.pi)
    draw_pentagram(-3*size, 6*size, size/6, math.atan(1/7)*180/math.pi)
    draw_pentagram(-3*size, 3*size, size/6, 0)
    draw_pentagram(-5*size, size, size/6, -(math.atan(4/5)*180/math.pi))


def main():
    size = 30
    turtle.speed(8)
    draw_square(30*size, 20*size)
    draw_five_pentagram(size)
    # draw_grid(30*size, 20*size, size)

    turtle.hideturtle()
    turtle.mainloop()


if __name__ == '__main__':
    main()