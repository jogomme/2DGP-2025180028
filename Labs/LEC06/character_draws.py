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

def move_rectangle(x, y) :
    print("rectangle")
    
    clear_canvas()

    ## draw_rectangle(200, 100, 600, 500, 0)

    if x < 600 and y <= 101:
        x += 1
    elif x <= 601 and y < 500 :
        y += 1
    elif x > 200 and y <= 501 :
        x -= 1
        
    character.draw(x, y)
    
    update_canvas()
    
    return x, y

def move_triangle() :
    print("triangle")
    
    clear_canvas()

    update_canvas()
    
    pass

while True :
    while angle <= 3 * math.pi / 2:
        angle, x, y = move_circle(angle= angle, radius= radius)
    delay(0.1)
    while True :
        x, y = move_rectangle(x, y)
    delay(2)
    move_triangle()
    delay(2)
    angle = -math.pi / 2

close_canvas()