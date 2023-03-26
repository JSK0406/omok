import sys
input = sys.stdin.readline

board_state = [[0 for _ in range(15)] for _ in range(15)]  # 15*15의 오목판 생성
dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def check_board(x, y, is_black):
    '''
    :param x: x 좌표
    :param y: y 좌표
    :param is_black: 현재 돌의 색깔
    :return: 게임이 끝났다면 False를 return하여 is_running에 대입
    '''
    color_num = 1 if is_black else 2  # 흑돌이면 1 백돌이면 2
    for di in range(8):
        cnt = 1
        next_y = y+dy[di]
        next_x = x+dx[di]
        while 0 <= next_y <= 14 and 0 <= next_x <= 14 and board_state[next_y][next_x] == color_num:
            cnt += 1
            next_y += dy[di]
            next_x += dx[di]
        if cnt >= 5:
            return False
    return True

is_running = True
is_black = True  # 선공에 따라 넣어주면 됨
while is_running:

    # 입력을 받아 게임판에 반영
    now_color = '흑돌' if is_black else '백돌'
    print(f'{now_color}차례입니다.')
    print('좌표를 입력해주세요 : ', end='')
    x, y = map(int, input().split())
    board_state[y-1][x-1] = 1 if is_black else 2  # 흑돌이면 1 / 백돌이면 2

    # 착수 후 게임판을 보여줌
    print('착수 후 상황')
    print('------------------------------')
    for row in board_state:
        print(*row)
    print('------------------------------')

    # 다음 차례를 위한 준비
    is_running = check_board(x-1, y-1, is_black)
    is_black = not is_black

print(f'승자는 {now_color}입니다!')