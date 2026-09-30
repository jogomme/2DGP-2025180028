from pico2d import *

open_canvas()

sonic = load_image("sonic-sprite.png")
background = load_image("grass.png")

frame_nomal = 9

frame_jump_up = 6
frame_jump_down = 2

frame_attack = 6

frame_roll = 9
frame_rolling = 6

def nomal() :
    pass

def jump() :
    pass

def attack() :
    pass

def roll() :
    pass

def rolling() :
    pass

running = True
pressed_inputs = set()
pressed_this_frame = set()
left_mouse_pressed = False
left_clicked = False

while running :
    pressed_this_frame.clear()
    left_clicked = False

    background.draw(400,30)
    
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key in (SDLK_w, SDLK_a, SDLK_s, SDLK_d, SDLK_SPACE):
                pressed_inputs.add(event.key)
                pressed_this_frame.add(event.key)
        elif event.type == SDL_KEYUP:
            pressed_inputs.discard(event.key)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                left_mouse_pressed = True
                left_clicked = True
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                left_mouse_pressed = False
                
    update_canvas()

close_canvas()