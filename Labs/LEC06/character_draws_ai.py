from pico2d import *
import math


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.01
MOVE_STEP = 1.0


def segment_positions(start, end, step=MOVE_STEP):
	start_x, start_y = start
	end_x, end_y = end
	distance = math.hypot(end_x - start_x, end_y - start_y)
	frame_count = max(1, math.ceil(distance / step))

	for frame in range(1, frame_count + 1):
		progress = frame / frame_count
		yield (
			start_x + (end_x - start_x) * progress,
			start_y + (end_y - start_y) * progress,
		)


def path_positions(waypoints):
	for start, end in zip(waypoints, waypoints[1:]):
		yield from segment_positions(start, end)


def circle_positions(center, radius, step=0.01):
	angle = -math.pi / 2
	end_angle = 3 * math.pi / 2

	while True:
		yield (
			center[0] + radius * math.cos(angle),
			center[1] + radius * math.sin(angle),
		)
		if angle >= end_angle:
			break
		angle = min(angle + step, end_angle)


def main():
	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	character = load_image('character.png')

	center = (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
	circle_path = circle_positions(center, 200)
	rectangle_path = path_positions([
		(400, 100), (600, 100), (600, 500),
		(200, 500), (200, 100), (400, 100),
	])
	triangle_path = path_positions([
		(400, 100), (600, 100), (400, 500),
		(200, 100), (400, 100),
	])

	try:
		while True:
			for motion_path in (circle_path, rectangle_path, triangle_path):
				for x, y in motion_path:
					events = get_events()
					if any(event.type == SDL_QUIT for event in events):
						return
					if any(
						event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
						for event in events
					):
						return

					clear_canvas()
					character.draw(x, y)
					update_canvas()
					delay(FRAME_DELAY)

				if motion_path is circle_path:
					circle_path = circle_positions(center, 200)
				elif motion_path is rectangle_path:
					rectangle_path = path_positions([
						(400, 100), (600, 100), (600, 500),
						(200, 500), (200, 100), (400, 100),
					])
				else:
					triangle_path = path_positions([
						(400, 100), (600, 100), (400, 500),
						(200, 100), (400, 100),
					])
	finally:
		close_canvas()


if __name__ == '__main__':
	main()
