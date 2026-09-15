## 여기를 채우시오.


from pico2d import *

# open_canvas 로 인해 800x600짜리 캔버스가 열린다.
open_canvas(800, 600)

# load_image('파일명') 으로 이미지를 가져옴
grass = load_image('grass.png')
character = load_image('character.png')

# 게임이 실행 중인지 알려주는 변수
is_game_on = True

Points = [200,100]

character.draw(Points[0], Points[1])


while is_game_on :
    # 백지 상태로 만들기
    clear_canvas()
    
    # 사각형의 경로 만들기
    draw_rectangle(200,100,600,500)
    
    # 조건문
    if Points[0] < 600 and Points[1] <= 100:
        Points[0] += 2
    elif Points[0] == 600 and Points[1] < 500 :
        Points[1] += 2
    elif Points[0] > 200 and Points[1] == 500 :
        Points[0] -= 2
    elif Points[0] == 200 and Points[1] > 100 :
        Points[1] -= 2
    
    character.draw(Points[0], Points[1])
    
    
    update_canvas()
    delay(0.01)
    
    events = get_events()

    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                is_game_on = False
    
        
# 캔버스를 닫는다.
close_canvas()