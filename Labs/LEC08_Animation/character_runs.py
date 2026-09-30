from pico2d import *

open_canvas()

grass = load_image('grass.png')
run_character = load_image('run_animation.png')
character = load_image('animation_sheet.png')

# fill here

frame = 0

def right_run() :
     run_character.clip_draw(
            frame * 100, 0, #left, bottom
            100, 100, # width, height
            x, 90, # destination x, y
            200, 200 # width, height
        )
     
def left_run() :
    run_character.clip_composite_draw(
                frame * 100, 0, #left, bottom
                100, 100, # width, height
                0, 'h',
                800 - x, 90, # destination x, y
                200, 200 # width, height
            )

def right_walk() :
    character.clip_draw(
            frame * 100, 300, #left, bottom
            100, 100, # width, height
            x, 90, # destination x, y
            200, 200 # width, height
        )

def left_walk() :
    character.clip_composite_draw(
                frame * 100, 700, #left, bottom
                100, 100, # width, height
                0, 'h',
                800 - x, 90, # destination x, y
                200, 200 # width, height
            )

while True :
    
    for x in range(0, 800, 5):
        clear_canvas()
        grass.draw(400, 30)
    
        right_run()
    
        update_canvas()

        frame = (frame + 1) % 8
        delay(0.05)

    for x in range(0, 800, 5):
        clear_canvas()
        grass.draw(400, 30)
    
        left_run()
    
        update_canvas()

        frame = (frame + 1) % 8
        delay(0.05)
        
    for x in range(0, 800, 5):
        clear_canvas()
        grass.draw(400, 30)
    
        right_walk()
    
        update_canvas()

        frame = (frame + 1) % 8
        delay(0.05)
    
    for x in range(0, 800, 5):
        clear_canvas()
        grass.draw(400, 30)
    
        left_walk()
    
        update_canvas()

        frame = (frame + 1) % 8
        delay(0.05)

close_canvas()

