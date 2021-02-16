import random


def showBoard(board):
    print("Current Game:")
    for i in board:
        for j in i:
            if j == 1:
                print("X", end=" ")
            elif j == 2:
                print("O", end=" ")
            else:
                print("-", end=" ")
        print()


def reset(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = 0


def Play(board, x, y, player, movesPlayer):
    if board[x][y] != 0:
        return [board, movesPlayer]
    else:
        movesPlayer += 1
        if player == 1:
            board[x][y] = 1
        else:
            board[x][y] = 2
    return [board, movesPlayer]


def CheckWin(board, player):
    # horizontal
    if board[0][1] == board[0][2] == board[0][0] == player:
        return player
    if board[1][1] == board[1][2] == board[1][0] == player:
        return player
    if board[2][1] == board[2][2] == board[2][0] == player:
        return player
    # vertical
    if board[1][0] == board[2][0] == board[0][0] == player:
        return player
    if board[1][1] == board[2][1] == board[0][1] == player:
        return player
    if board[1][2] == board[2][2] == board[0][2] == player:
        return player
    # obliques
    if board[0][0] == board[1][1] == board[2][2] == player:
        return player
    if board[0][2] == board[1][1] == board[2][0] == player:
        return player
    return 0


def Greetings():
    print("Welcome to tic tac toe!\n")


def OneVsOne(r, first):
    movesPlayer = InitMoves()
    Table1 = CreateEmptyBoard()
    showBoard(Table1)
    current = first
    sai = False
    while not sai and sum(movesPlayer) < 9:
        i = movesPlayer[current - 1]
        while i == movesPlayer[current - 1]:
            if r:
                [x, y] = ranMove(current)
            else:
                [x, y] = askMove(current)
            [Table1, movesPlayer[current - 1]] = Play(Table1, x, y, current, movesPlayer[current - 1])
            if i == movesPlayer[current - 1]:
                print ("Invalid Move")
        showBoard(Table1)
        if CheckWin(Table1, current) == current:
            sai = True
        else:
            current = changeCurrent(current)
    if sai:
        print("Player", current, "win")
    else:
        current = 0
        print("Tie")
    return current


def askMove(player):
    print("\nPlayer", player, ":\n")
    while 1:
        a = int(input("Row:"))
        b = int(input("Column:"))
        if 1 <= a < 4 and 1 <= b < 4:
            return [a - 1, b - 1]
        else:
            print("\nInvalid Move!\n")


def ranMove(player):
    print("\nPlayer", player, ":\n")
    while 1:
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        return [a, b]


def CreateEmptyBoard():
    return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def InitMoves():
    return [0, 0]


def ChooseGameMode():
    print("Choose Game Mode:\n1: 1 vs 1\n2: Simulation Mode")
    x = 3
    while x < 1 or x > 2:
        x = int(input("Your Chose:"))
    return x


def whofirst():
    print("\nFirst to play?\n0: random\n1: Player 1\n2: Player 2\n")
    x = 3
    while x < 0 or x > 2:
        x = int(input("Your Chose:"))
    if x == 0:
        x = random.randint(1, 2)
    return x


def changeCurrent(current):
    if current == 1:
        return 2
    else:
        return 1


def stats(array):
    print("\n\nStats:\nPlayer 1:", array[1], "\nPlayer 2:", array[2], "\nTie:", array[0])


def main():
    Greetings()
    gamemode = ChooseGameMode()
    wins = [0, 0, 0]
    current = 1
    if gamemode == 2:
        games = int(input("Games:"))
        for i in range(games):
            current = changeCurrent(current)
            winner = OneVsOne(1, current)
            wins[winner] += 1
    elif gamemode == 1:
        response = 'y'
        another = 1
        while another:
            current = whofirst()
            winner = OneVsOne(0, current)
            wins[winner] += 1
            while not (response == 'y' or response == 'Y' or response == 'N' or response == 'n'):
                response = input("New Game?\n Y-Yes  N-No  :")
            if response == 'N' or response == 'n':
                another = 0
    stats(wins)
    return 0


if __name__ == "__main__":
    main()
