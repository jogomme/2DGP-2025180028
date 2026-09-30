from pico2d import *
import time

open_canvas()

sonic = load_image("sonic-sprite.png")
background = load_image("grass.png")

normal_frames = [
    (1, 39, 29, 39), (31, 40, 26, 38), (58, 39, 28, 39),
    (86, 40, 30, 38), (118, 40, 30, 38), (150, 40, 30, 38),
    (182, 40, 29, 38), (211, 39, 29, 38), (240, 39, 29, 38),
    (270, 45, 24, 32), (302, 51, 29, 26)
]
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
animations = {
    "normal": normal_frames,
    "run": run_frames,
    "jump": jump_frames,
    "attack": attack_frames,
    "roll": roll_frames,
    "rolling": rolling_frames,
}
animation_order = ["normal", "run", "jump", "attack", "roll", "rolling"]
animation_indices = {name: 0 for name in animations}

def draw_animation_frame(animation_name, frame_index, destination_height=300):
    frame_left, frame_top, frame_width, frame_height = animations[animation_name][frame_index]
    destination_width = frame_width * destination_height // frame_height
    sonic.clip_draw(
        frame_left, sonic.h - frame_top - frame_height,
        frame_width, frame_height,
        400, 300,
        destination_width, destination_height
    )

def play_animation_frame(animation_name, destination_height=300):
    frame_index = animation_indices[animation_name]
    draw_animation_frame(animation_name, frame_index, destination_height)
    animation_indices[animation_name] = (frame_index + 1) % len(animations[animation_name])
    return animation_indices[animation_name] == 0

def nomal() :
    return play_animation_frame("normal")

def run():
    return play_animation_frame("run")

def jump() :
    return play_animation_frame("jump")

def attack() :
    return play_animation_frame("attack")

def roll() :
    return play_animation_frame("roll")

def rolling() :
    return play_animation_frame("rolling")

def get_requested_animation():
    if SDLK_SPACE in pressed_inputs:
        return "jump"
    if left_clicked or left_mouse_pressed:
        return "attack"
    if SDLK_a in pressed_inputs or SDLK_d in pressed_inputs:
        return "roll"
    if SDLK_w in pressed_inputs:
        return "run"
    if SDLK_s in pressed_inputs:
        return "rolling"
    return None

animation_functions = {
    "normal": nomal,
    "run": run,
    "jump": jump,
    "attack": attack,
    "roll": roll,
    "rolling": rolling,
}

repeats_per_animation = 5
pause_duration = 1.0
animation_order_index = 0
completed_repeats = 0
pause_until = None
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

    requested_animation = get_requested_animation()
    if requested_animation is not None:
        animation_functions[requested_animation]()
    elif pause_until is not None:
        if time.monotonic() < pause_until:
            animation_name = animation_order[animation_order_index]
            draw_animation_frame(animation_name, len(animations[animation_name]) - 1)
        else:
            pause_until = None
            animation_order_index = (animation_order_index + 1) % len(animation_order)
            completed_repeats = 0
            animation_name = animation_order[animation_order_index]
            animation_indices[animation_name] = 0
    else:
        animation_name = animation_order[animation_order_index]
        if animation_functions[animation_name]():
            completed_repeats += 1
            if completed_repeats >= repeats_per_animation:
                pause_until = time.monotonic() + pause_duration
                
    update_canvas()
    delay(0.05)

close_canvas()