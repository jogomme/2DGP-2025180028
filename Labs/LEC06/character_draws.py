# 실습 과제 진행

from pico2d import *
import math

wide = 800
height = 600

open_canvas(wide,height)

character = load_image('character.png')

radius = 200
angle = 0

Points = [wide / 2, height / 2, radius]

def move_circle(angle, radius) :
    print(f"circle")
    
    clear_canvas()
    
    x = Points[0] + radius * math.cos(angle)
    y = Points[1] + radius * math.sin(angle)
    
    character.draw(x, y)
    
    update_canvas()
    
    angle += 0.01
    
    return angle

def move_rectangle() :
    print("rectangle")
    pass

def move_triangle() :
    print("triangle")
    pass

while True :
    while angle <= 2 * math.pi :
        angle = move_circle(angle= angle, radius= radius)
    delay(2)
    move_rectangle()
    move_triangle()
    pass

close_canvas()