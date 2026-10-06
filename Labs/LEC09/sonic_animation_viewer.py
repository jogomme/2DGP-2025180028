"""Play the Sonic sprite sheet animations in sequence."""

from pico2d import *


WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720


def get_sprite_path():
    return Path(__file__).resolve().with_name("sonic-sprite.png")


def main():
    sprite_path = get_sprite_path()
    if not sprite_path.is_file():
        raise FileNotFoundError(f"Sprite sheet not found: {sprite_path}")

    open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)
    try:
        try:
            sprite_sheet = load_image(str(sprite_path))
        except IOError as error:
            raise RuntimeError(f"Unable to load sprite sheet: {sprite_path}") from error

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
