import random


def check_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):
        if all(row[col] == symbol for row in board):
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol or board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


print('Давай сыграем в крестики нолики?  ')

alllines = [['|', '|', '|'], ['|', '|', '|'], ['|', '|', '|']]


def print_board():
    for row in alllines:
        for col in row:
            spaces = 2
            spaces -= (len(col) - 1)
            print(col, end=" " * spaces)
        print()


print_board()

while True:
    index = int(input('Выбери номер места, куда поставить крестик  '))
    row = (index - 1) // 3
    col = (index - 1) % 3
    if alllines[row][col] == '|':
        alllines[row][col] = 'X'
        print_board()
        if check_winner(alllines, 'X'):
            print("Ты выиграл!")
            break
        available_moves = [(i, j) for i in range(3) for j in range(3) if alllines[i][j] == '|']
        if available_moves:
            print()
            print('Теперь мой ход')
            print()
            move = random.choice(available_moves)
            alllines[move[0]][move[1]] = 'O'
            print_board()
            if check_winner(alllines, 'O'):
                print("Компьютер выиграл!")
                break
        else:
            print("Все места заняты. Ничья.")
            break
    else:
        print("Это место уже занято. Пожалуйста, выберите другое место.")
