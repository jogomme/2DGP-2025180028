"""Play the Sonic sprite sheet animations in sequence."""

import time
from pathlib import Path

from pico2d import *


WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720
DISPLAY_SCALE = 8
FRAME_DURATION = 0.08
REPEATS_PER_ACTION = 5
PAUSE_DURATION = 1.0
NORMAL_FRAMES = (
    (1, 39, 29, 39),
    (31, 40, 26, 38),
    (58, 39, 28, 39),
    (86, 40, 30, 38),
    (118, 40, 30, 38),
    (150, 40, 30, 38),
    (182, 40, 29, 38),
    (211, 39, 29, 38),
    (240, 39, 29, 38),
    (270, 45, 24, 32),
    (302, 51, 29, 26),
)
RUN_FRAMES = (
    (8, 80, 26, 37),
    (37, 80, 27, 37),
    (65, 80, 31, 38),
    (97, 80, 37, 37),
    (135, 80, 32, 35),
    (170, 79, 32, 38),
    (206, 79, 26, 38),
    (238, 80, 24, 37),
    (263, 80, 30, 37),
    (295, 80, 36, 37),
    (334, 80, 32, 36),
    (370, 79, 29, 38),
)
JUMP_FRAMES = (
    (1, 124, 33, 40),
    (39, 124, 35, 39),
    (89, 125, 35, 38),
    (130, 121, 34, 42),
    (181, 122, 34, 41),
    (228, 122, 33, 40),
)
ATTACK_FRAMES = (
    (1, 239, 29, 35),
    (36, 239, 30, 35),
    (74, 239, 31, 35),
    (111, 238, 31, 36),
    (149, 239, 30, 35),
    (186, 238, 31, 36),
)
ROLL_FRAMES = (
    (1, 169, 29, 30),
    (36, 167, 28, 31),
    (67, 169, 30, 29),
    (98, 170, 31, 28),
    (131, 168, 29, 30),
    (162, 168, 29, 31),
    (193, 170, 30, 29),
    (230, 170, 31, 28),
    (268, 170, 30, 30),
)
ROLLING_FRAMES = (
    (1, 206, 30, 27),
    (36, 206, 29, 27),
    (70, 206, 29, 27),
    (105, 206, 29, 27),
    (139, 206, 29, 27),
    (174, 206, 29, 27),
)
SPIN_ATTACK_FRAMES = (
    (1, 283, 29, 35),
    (36, 283, 30, 35),
    (72, 286, 39, 31),
    (123, 285, 39, 32),
    (172, 286, 39, 31),
    (218, 285, 38, 32),
)
TURNAROUND_FRAMES = (
    (1, 326, 24, 45),
    (31, 327, 29, 44),
    (65, 327, 20, 44),
    (90, 327, 25, 43),
    (119, 327, 25, 43),
    (149, 327, 20, 44),
)
IMPACT_FRAMES = (
    (184, 341, 40, 28),
    (232, 341, 39, 27),
)
RUN_ALT_FRAMES = (
    (1, 379, 27, 38),
    (31, 379, 31, 36),
    (64, 379, 31, 36),
    (99, 377, 33, 38),
    (136, 379, 32, 36),
    (176, 379, 33, 36),
    (217, 379, 33, 36),
    (254, 378, 33, 36),
)
REACTION_FRAMES = (
    (6, 429, 34, 40),
    (49, 426, 34, 43),
    (96, 427, 23, 39),
    (125, 427, 23, 39),
)

ANIMATIONS = {
    "normal": NORMAL_FRAMES,
    "run": RUN_FRAMES,
    "jump": JUMP_FRAMES,
    "attack": ATTACK_FRAMES,
    "roll": ROLL_FRAMES,
    "rolling": ROLLING_FRAMES,
    "spin_attack": SPIN_ATTACK_FRAMES,
    "turnaround": TURNAROUND_FRAMES,
    "impact": IMPACT_FRAMES,
    "run_alt": RUN_ALT_FRAMES,
    "reaction": REACTION_FRAMES,
}
ANIMATION_ORDER = tuple(ANIMATIONS)


def get_sprite_path():
    return Path(__file__).resolve().with_name("sonic-sprite.png")


def draw_frame(sprite_sheet, frame, scale=1):
    left, top, width, height = frame
    sprite_sheet.clip_draw(
        left,
        sprite_sheet.h - top - height,
        width,
        height,
        WINDOW_WIDTH // 2,
        WINDOW_HEIGHT // 2,
        width * scale,
        height * scale,
    )


def get_animation_frame(frames, frame_index):
    return frames[frame_index]


class AnimationPlayer:
    def __init__(self):
        self.action_index = 0
        self.frame_index = 0
        self.completed_repeats = 0
        self.phase = "playing"
        self.pause_until = None

    @property
    def action_name(self):
        return ANIMATION_ORDER[self.action_index]

    @property
    def current_frame(self):
        return get_animation_frame(ANIMATIONS[self.action_name], self.frame_index)

    def advance_frame(self, now):
        if self.phase == "paused":
            if now >= self.pause_until:
                self.advance_action()
            return False
        if self.phase != "playing":
            return False

        frames = ANIMATIONS[self.action_name]
        if self.frame_index + 1 == len(frames):
            self.completed_repeats += 1
            if self.completed_repeats == REPEATS_PER_ACTION:
                self.phase = "paused"
                self.pause_until = now + PAUSE_DURATION
                return True

            self.frame_index = 0
            return True

        self.frame_index += 1
        return False

    def advance_action(self):
        self.action_index = (self.action_index + 1) % len(ANIMATION_ORDER)
        self.frame_index = 0
        self.completed_repeats = 0
        self.pause_until = None
        self.phase = "playing"


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
        player = AnimationPlayer()
        next_frame_at = time.monotonic() + FRAME_DURATION
        while running:
            for event in get_events():
                if event.type == SDL_QUIT:
                    running = False
                elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                    running = False

            now = time.monotonic()
            while now >= next_frame_at:
                player.advance_frame(next_frame_at)
                if player.phase == "paused":
                    next_frame_at = player.pause_until
                else:
                    next_frame_at += FRAME_DURATION

            clear_canvas()
            draw_frame(sprite_sheet, player.current_frame, DISPLAY_SCALE)
            update_canvas()
            delay(0.01)
    finally:
        close_canvas()

if __name__ == "__main__":
    main()
