# 2021184035 지민우
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
dir = 0     # 캐릭터의 바라보는 방향을 이동 방향과 일치시키기 위한 변수
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow.draw(hand_x, hand_y)     # (hand_x, hand_y)에 손화살표 그리기
    character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)     # dir 값에 따라 캐릭터의 바라보는 방향을 변경하도록 수정
    update_canvas()
    frame = (frame + 1) % 8

    if t == 0:              # t 값이 0일 때(캐릭터가 손화살표로 움직이기 시작할 때) 방향을 바꾸도록 함
        if hand_x > x:      # 손화살표의 x좌표가 캐릭터의 x좌표보다 클 경우(손화살표가 캐릭터보다 오른쪽에 있을 경우)
            dir = 1         # 캐릭터의 바라보는 방향을 오른쪽으로
        else:               # 아닌 경우
            dir = 0         # 캐릭터의 바라보는 방향을 왼쪽으로

    # 식 m(t) = (1 - t)*p1 + t * p2 로 캐릭터의 좌표를 계산 / p1 : 캐릭터의 위치, p2 : 손화살표의 위치
    x = (1 - t) * x + t * hand_x
    y = (1 - t) * y + t * hand_y

    t += speed      # t 값을 speed(이동 속도)만큼 점진적으로 증가

    if t >= 1.0:    # t 값이 1.0이 되면(캐릭터가 손화살표 위치에 도달하면)
        t = 0.0     # t 값을 0.0으로 설정하여 그 위치를 캐릭터의 시작 위치로 설정하고
        hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)    # 손화살표의 좌표를 랜덤하게 재설정

    handle_events()

    delay(0.02)

close_canvas()