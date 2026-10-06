"""Play the Sonic sprite sheet animations in sequence."""

from pico2d import *


WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720


def main():
    open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    try:
        running = True
        while running:
            for event in get_events():
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    running = False

            clear_canvas()
            update_canvas()
            delay(0.01)
    finally:
        close_canvas()

if __name__ == "__main__":
    main()
