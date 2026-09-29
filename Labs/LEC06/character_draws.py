# 실습 과제 진행

from pico2d import *
import math

wide = 800
height = 600

open_canvas(wide,height)

character = load_image('character.png')

radius = 200
angle = -math.pi / 2

Points = [wide / 2, height / 2, radius]



def move_circle(angle, radius) :
    print(f"circle")
    
    clear_canvas()
    
    x = Points[0] + radius * math.cos(angle)
    y = Points[1] + radius * math.sin(angle)
    
    character.draw(x, y)
    
    update_canvas()
    
    angle += 0.01
    
    return angle, x, y

def move_rectangle(x, y, direction) :
    print("rectangle")
    
    clear_canvas()

    ## draw_rectangle(200, 100, 600, 500, 0)

    if direction == 0:
        x += 1
        if x >= 600:
            x = 600
            direction = 1

    elif direction == 1:
        y += 1
        if y >= 500:
            y = 500
            direction = 2

    elif direction == 2:
        x -= 1
        if x <= 200:
            x = 200
            direction = 3

    elif direction == 3:
        y -= 1
        if y <= 100:
            y = 100
            direction = 4
            
    elif direction == 4 :
        x += 1
        if x >= 400 :
            x = 400
            direction = 5
            
    character.draw(x, y)
    
    update_canvas()
    
    return x, y, direction

def move_triangle(x, y, direction):
    print("triangle")

    TrianglePoint = [[wide / 2, 500],
                 [200, 100],
                 [600, 100]]
    # wide / 2, 500
    # 200, 100
    # 600, 100

    clear_canvas()

    if direction == 0 :
        x += 1
        if x >= 600:
            x = 600
            direction = 1
    
    elif direction == 1 :
        y += 1
        x -= 0.5
        if x <= wide / 2 and y >= 500 :
            x = wide / 2
            y = 500
            direction = 2
            
    elif direction == 2 :
        y -= 1
        x -= 0.5
        if x <= 200 and y <= 100 :
            x = 200
            y = 100
            direction = 3
            
    elif direction == 3 :
        x += 1
        if x >= wide / 2 :
            direction = 4
            
    character.draw(x,y)

    update_canvas()

    return x, y, direction

while True :
    while angle <= 3 * math.pi / 2:
        angle, x, y = move_circle(angle= angle, radius= radius)
    delay(0.1)
    dir = 0
    while dir < 5 :
        x, y, dir = move_rectangle(x, y, dir)
    delay(0.1)
    dir = 0
    while dir < 4:
        x, y, dir = move_triangle(x, y, dir)
    delay(2)
    angle = -math.pi / 2

close_canvas()