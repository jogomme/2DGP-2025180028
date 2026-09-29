# 실습 과제 진행

from pico2d import *

wide = 800
height = 600

open_canvas(wide,height)

character = load_image('character.png')

def move_circle() :
    print(f"circle")
    clear_canvas()
    character.draw(400,300)
    update_canvas()
    pass

def move_rectangle() :
    print("rectangle")
    pass

def move_triangle() :
    print("triangle")
    pass

while True :
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()