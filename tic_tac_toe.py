# 1. 자료구조
#화면에 보여줄 보드
board_screen = '0 | 1 | 2 \n3 | 4 | 5 \n6 | 7 | 8\n'
# 게임의 진행 상태
board = [" "] * 9
# 이겼을 때의 상태
win_status = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
              (0, 3, 6), (1, 4, 7), (2, 5, 8),
              (0, 4, 8), (2, 4, 6)]
player = 'O'
computer = 'X'

# 2. 필요한 함수 정의
def showBoard():
    print(board_screen)

def updateGame(who, number):
    global board, board_screen
    board[number] = who
    board_screen = board_screen.replace(str(number), who)
    # print(who, number)

def getComputerNumber():
    for i in range(len(board)):
        if board[i] == " ":
            return i
    return -1

def isWin(turn):
    for status in win_status:
        a, b, c = status

        if board[a] == board[b] == board[c] == turn:
            return True

    return False

# 3. 메인 로직
# 3-1. 필요한 자료구조 초기화
print('========== Tic-Tac-Toe ==========')
# 3-2. 보드를 보여줌
showBoard()
while True:

    # 3-3. Player 차례
    # player 입력 받아서 처리
    player_input = int(input('숫자를 입력하세요 :'))

    # 잘못된 숫자 방지
    if player_input < 0 or player_input > 8:
        print('0~8 사이 숫자를 입력하세요')
        continue

    # 이미 선택된 자리 방지
    if board[player_input] != " ":
        print('이미 선택된 자리입니다')
        continue

    updateGame(player, player_input)
    showBoard()

    if isWin(player):
        # Player가 이겼음
        print('You Win')
        break

    # 3-4. 컴퓨터 차례
    # computer가 놓을 자리를 선택
    computer_input = getComputerNumber()

    if computer_input == -1:
        # 비겼음
        print('Draw')
        break

    updateGame(computer, computer_input)
    showBoard()

    if isWin(computer):
        # 컴퓨터가 이겼음
        print('You Lose')
        break