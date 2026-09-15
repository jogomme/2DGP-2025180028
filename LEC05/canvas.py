## 여기를 채우시오.


from pico2d import *
import math

# open_canvas 로 인해 800x600짜리 캔버스가 열린다.
open_canvas(800, 600)

# load_image('파일명') 으로 이미지를 가져옴
grass = load_image('grass.png')
character = load_image('character.png')

# 게임이 실행 중인지 알려주는 변수
is_game_on = True

radius = 200
wide = 800
height = 600

Points = [wide / 2, height / 2, radius]
character.draw(Points[0], Points[1])

angle = 0


while is_game_on :
    # 백지 상태로 만들기
    clear_canvas()
    
    # 원 경로 만들기
    draw_circle(wide / 2, height / 2, radius)
    
    # 조건문
    x = Points[0] + radius * math.cos(angle)
    y = Points[1] + radius * math.sin(angle)
    character.draw(x, y)

    update_canvas()
    
    angle += 0.01
    
    delay(0.01)
    
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                is_game_on = False
    
        
# 캔버스를 닫는다.
close_canvas()