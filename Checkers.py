import time

RED = 0
BLUE = 1
BOTH = 2

PLAYER_1_PIECE = "🔴"
PLAYER_2_PIECE = "🔵"
EMPTY_SQUARE = "⚫"
UNREACHABLE_SQUARE = "⚪"


def pieces(board, type):
    target = ((PLAYER_1_PIECE),(PLAYER_2_PIECE),(PLAYER_1_PIECE,PLAYER_2_PIECE))[type] # Look for red, blue or both
    locations = []
    for i in range(0, 8):
        for j in range(0, 8):
            if board[i][j] in target:
                locations.append((i, j))

    return locations


def showBoard(board, side=RED):
    if side == RED:
        for i in board[::-1]:
            for j in i:
                print(j, end=" ")
            print()
        print("a   b  c  d  e   f  g  h")

    else:
        for i in board:
            for j in i[::-1]:
                print(j, end=" ")
            print()
        print("h   g  f  e  d   c  b  a")

def pieceMovesRed(board, i, j):
    # Both side capture, if no capture then both side single
    capture = False
    valid = []
    if i+2<=7:
        if (j - 2 >= 0):
            if board[i + 1][j - 1] == PLAYER_2_PIECE and board[i + 2][j - 2] == EMPTY_SQUARE:
                capture = True
                valid.append((i + 2, j - 2))

        if (j + 2 <= 7):
            if board[i + 1][j + 1] == PLAYER_2_PIECE and board[i + 2][j + 2] == EMPTY_SQUARE:
                capture = True
                valid.append((i + 2, j + 2))
    if not capture and i+1<=7:
        if (j - 1 >= 0):
            if board[i + 1][j - 1] == EMPTY_SQUARE:
                valid.append((i + 1, j - 1))

        if (j + 1 <= 7):
            if board[i + 1][j + 1] == EMPTY_SQUARE:
                valid.append((i + 1, j + 1))

    return capture, valid


def pieceMovesBlue(board, i, j):
    # Both side capture, if no capture then both side single
    capture = False
    valid = []
    if i-2>=0:
        if (j - 2 >= 0):
            if board[i - 1][j - 1] == PLAYER_1_PIECE and board[i - 2][j - 2] == EMPTY_SQUARE:
                capture = True
                valid.append((i - 2, j - 2))

        if (j + 2 <= 7):
            if board[i - 1][j + 1] == PLAYER_1_PIECE and board[i - 2][j + 2] == EMPTY_SQUARE:
                capture = True
                valid.append((i - 2, j + 2))
    if not capture and i-1>=0:
        if (j - 1 >= 0):
            if board[i - 1][j - 1] == EMPTY_SQUARE:
                valid.append((i - 1, j - 1))

        if (j + 1 <= 7):
            if board[i - 1][j + 1] == EMPTY_SQUARE:
                valid.append((i - 1, j + 1))

    return capture, valid


def validFinder(board, side, previousJumpLocation):
    validMoves = []
    if side == RED:
        for piece in pieces(board, RED):
            a, b = pieceMovesRed(board, *piece)
            if len(b):
                for destination in b:
                    validMoves.append((a,piece,destination))
    else:
        for piece in pieces(board, BLUE):
            a, b = pieceMovesBlue(board, *piece)
            if len(b):
                for destination in b:
                    validMoves.append((a,piece,destination))

    if any(move[0] for move in validMoves): # Only allow captures if capture possible
        validMoves = [move for move in validMoves if move[0]]

    if previousJumpLocation:
        validMoves = [move for move in validMoves if move[1] == previousJumpLocation]

    return validMoves




blank_board = []
squares = [EMPTY_SQUARE,UNREACHABLE_SQUARE,PLAYER_1_PIECE,PLAYER_2_PIECE]
board = []
for i in range(0, 8):
    blank_board.append([])
    for j in range(0, 8):
        blank_board[i].append(squares[(i+j) % 2])

for i in range(0, 8):
    board.append(blank_board[i].copy())
    for j in range(0, 8):
        if i < 3:
            if not ((i+j) % 2):
                board[i][j] = PLAYER_1_PIECE
        if i > 4:
            if not ((i + j) % 2):
                board[i][j] = PLAYER_2_PIECE

for i in blank_board[::-1]:
    for j in i:
        print(j, end=" ")
    print()
print("\n")



running = True
current_move = RED
success = False
previousJumpLocation = None

while pieces(board, RED) and pieces(board, BLUE):
    success = True
    showBoard(board, current_move)

    validMoves = validFinder(board, current_move, previousJumpLocation)





    for move in validMoves:
        print(chr(move[1][1] + ord('a')), end="")
        print(move[1][0] + 1, end=", ")
        print(chr(move[2][1] + ord('a')), end="")
        print(move[2][0] + 1)



    try:
        inputMove = input("Enter your move: ")
        location1 = (int(inputMove[1]) - 1, ord(inputMove[0]) - ord('a'))
        location2 = (int(inputMove[5]) - 1, ord(inputMove[4]) - ord('a'))
        for i in location1+location2:
            if not (0 <= i <= 7):
                raise Exception

        if any((move[1] == location1 and move[2] == location2) for move in validMoves):
            location1 = (int(inputMove[1]) - 1, ord(inputMove[0]) - ord('a'))
            location2 = (int(inputMove[5]) - 1, ord(inputMove[4]) - ord('a'))

            board[location2[0]][location2[1]] = board[location1[0]][location1[1]]
            board[location1[0]][location1[1]] = EMPTY_SQUARE

            if (validMoves[0][0]): # Capture (if first is true, all true)
                board[((location2[0] - location1[0]) // 2) + location1[0]][((location2[1] - location1[1]) // 2) + location1[1]] = EMPTY_SQUARE

                if future := validFinder(board, current_move, location2):
                    if future[0][0]:
                        success = False
                        previousJumpLocation = location2

        else:
            raise Exception





    except:
        print("Invalid move")
        success = False




    if success:
        previousJumpLocation = None
        if current_move == RED:
            current_move = BLUE
        else:
            current_move = RED
            time.sleep(0.5)


    print()