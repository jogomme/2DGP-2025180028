import game_world
from pico2d import get_canvas_width, load_image


class Ball:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 10
        self.image = load_image('ball21x21.png')
        if direction == -1 :
            print(f"공 발사 : 왼쪽 {direction}")
        else :
            print(f"공 발사 : 오른쪽 {direction}")

    def update(self):
        self.x += self.direction * self.speed
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
