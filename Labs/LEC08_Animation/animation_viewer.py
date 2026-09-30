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
run_frames = [
    (8, 80, 26, 37), (37, 80, 27, 37), (65, 80, 31, 38),
    (97, 80, 37, 37), (135, 80, 32, 35), (170, 79, 32, 38),
    (206, 79, 26, 38), (238, 80, 24, 37), (263, 80, 30, 37),
    (295, 80, 36, 37), (334, 80, 32, 36), (370, 79, 29, 38)
]
jump_frames = [
    (1, 124, 33, 40), (39, 124, 35, 39), (89, 125, 35, 38),
    (130, 121, 34, 42), (181, 122, 34, 41), (228, 122, 33, 40)
]
attack_frames = [
    (1, 239, 29, 35), (36, 239, 30, 35), (74, 239, 31, 35),
    (111, 238, 31, 36), (149, 239, 30, 35), (186, 238, 31, 36)
]
roll_frames = [
    (1, 169, 29, 30), (36, 167, 28, 31), (67, 169, 30, 29),
    (98, 170, 31, 28), (131, 168, 29, 30), (162, 168, 29, 31),
    (193, 170, 30, 29), (230, 170, 31, 28), (268, 170, 30, 30)
]
rolling_frames = [
    (1, 206, 30, 27), (36, 206, 29, 27), (70, 206, 29, 27),
    (105, 206, 29, 27), (139, 206, 29, 27), (174, 206, 29, 27)
]

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