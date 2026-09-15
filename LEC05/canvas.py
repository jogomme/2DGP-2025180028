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

chatacter = load_image('character.png')
chatacter.draw(400,300)
chatacter.draw(300,200)
chatacter.draw(500,400)

# 매 프레임마다 update__canvas()를 해줘야 한다
update_canvas()

# 5초 지연
delay(5)

# 캔버스를 닫는다.
close_canvas()