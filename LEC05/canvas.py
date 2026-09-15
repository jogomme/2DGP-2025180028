## 여기를 채우시오.


from pico2d import *

# open_canvas 로 인해 800x600짜리 캔버스가 열린다.
'''
좌표계 
(0,599) 

       
             (400,300)


(0,0)                          (799,0)
'''

open_canvas(800, 600)

# load_image('파일명') 으로 이미지를 가져옴
grass = load_image('grass.png')
character = load_image('character.png')

x = 0

while x < 800 :
    #캔버스를 지워준다
    clear_canvas()
    
    # 배경과 캐릭터 중 배경을 먼저 그려야 한다.
    # 그래야 캐릭터가 배경에 가려지지 않는다.
    grass.draw(400, 30)
    character.draw(x, 90)
    
    # 매 프레임마다 update__canvas()를 해줘야 한다
    update_canvas()
    x += 2
    delay(0.01)
    
# 캔버스를 닫는다.
close_canvas()