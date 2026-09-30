from pico2d import *

open_canvas()

sonic = load_image("sonic-sprite.png")
background = load_image("grass.png")

frame_jump_up = 6
frame_jump_down = 2

frame_attack = 6

frame_roll = 9
frame_rolling = 6

width = 40
height = 40
normal_frames = [
    (1, 39, 29, 39), (31, 40, 26, 38), (58, 39, 28, 39),
    (86, 40, 30, 38), (118, 40, 30, 38), (150, 40, 30, 38),
    (182, 40, 29, 38), (211, 39, 29, 38), (240, 39, 29, 38),
    (270, 45, 24, 32), (302, 51, 29, 26)
]
frame_nomal = len(normal_frames)

x = 0
normal_frame = 0

def nomal() :
    global normal_frame
    frame_left, frame_top, frame_width, frame_height = normal_frames[normal_frame]
    sonic.clip_draw(
        frame_left, sonic.h - frame_top - frame_height,
        frame_width, frame_height,
        400, 120,
        frame_width * 100 // frame_height, 100
    )
    normal_frame = (normal_frame + 1) % frame_nomal

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

    clear_canvas()
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

    if SDLK_SPACE in pressed_inputs:
        jump()
    elif left_clicked or left_mouse_pressed:
        attack()
    elif SDLK_a in pressed_inputs or SDLK_d in pressed_inputs:
        roll()
    else:
        nomal()
                
    update_canvas()
    delay(0.05)

close_canvas()