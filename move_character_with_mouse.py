from pico2d import *
import random   # random.randint 사용을 위한 random 모듈

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)    # 손화살표의 좌표 x, y(0부터 배경 너비와 높이 사이 랜덤한 값)
frame = 0
t = 0.0       # t = 0.0 : 캐릭터 시작 위치, t = 1.0 : 손화살표 위치 도달, 0 <= t <= 1
speed = 0.01  # 캐릭터 이동 속도
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(hand_x, hand_y)     # (hand_x, hand_y)에 손화살표 그리기
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8

    # 식 m(t) = (1 - t)*p1 + t * p2 로 캐릭터의 좌표를 계산 / p1 : 캐릭터의 위치, p2 : 손화살표의 위치
    x = (1 - t) * x + t * hand_x
    y = (1 - t) * y + t * hand_y

    t += speed      # t 값을 speed(이동 속도)만큼 점진적으로 증가

    handle_events()

    delay(0.05)

close_canvas()