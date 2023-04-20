board_row0 = [' ', '0', '1', '2']
board_row1 = ['0', '-', '-', '-']
board_row2 = ['1', '-', '-', '-']
board_row3 = ['2', '-', '-', '-']

print('Крестики-нолики. Новая игра')
print(' '.join(map(str, board_row0)))
print(' '.join(map(str, board_row1)))
print(' '.join(map(str, board_row2)))
print(' '.join(map(str, board_row3)))

rows_and_cols = ["0", "1", "2"]
xs_and_os = ['x', 'х', 'о', 'o', 0, "0", 'X', 'Х', "O", "О"]
xs = ['x', 'х', 'X', 'Х']
os = ['о', 'o', 0, "0", "O", "О"]
real_X = 'X'
real_O = 'O'
list_of_positions = []

x = None
y = None
move = None
counter = 0


def choose_and_check_position():
    global x, y
    while True:
        x, y = input('Введите номер строки (0, 1, 2): '), input('Введите номер столбца(0, 1, 2): ')
        if x in rows_and_cols and y in rows_and_cols and (int(x), int(y)) not in list_of_positions:
            print(f'Указатель на клетке {x}:{y}', "\n")
            list_of_positions.append((int(x), int(y)))
            break
        else:
            print('Некорректный ввод или попытка занять непустую клетку. Попробуйте еще раз: ')
            continue
    return x, y

def choose_x_or_o():
    global move, counter

    while True:
        if counter == 0:
            move = str.upper(input('Первый ход. Начинают "крестики": '))
            if move in xs:
                print(f'Ставим {real_X} на клетку {x}:{y} ')
                counter = counter + 1
                move = real_X
                return move

            else:
                print("Что-то не так, попробуйте еще. Возможно, введен не крестик (х/Х) ")
                print('\n')
                continue

        if counter % 2 == 0 and counter != 0:
            move = str.upper(input('Ход "крестиков": '))
            if move in xs:
                print(f'Ставим {real_X} на клетку {x}:{y} ')
                counter = counter + 1
                move = real_X
                return move

            else:
                print("Что-то не так, попробуйте еще. Возможно, введен не крестик (х/Х) ")
                print('\n')
                continue
        if counter % 2 == 1:
            move = str.upper(input('Ход "ноликов": '))
            if move in os:
                print(f'Ставим {real_O} на клетку {x}:{y} ')
                counter = counter + 1
                move = real_O
                return move

            else:
                print("Что-то не так, попробуйте еще. Возможно, введен не нолик (o/O/0) ")
                print('\n')
                continue
        else:
            print("Что-то не так, попробуйте еще. ")
            continue

    return counter


def place_x_or_o():
    global board_row1, board_row2, board_row3
    if x == '0':
        ind = int(y) + 1
        board_row1.pop(ind)
        board_row1.insert(ind, move)

    if x == '1':
        ind = int(y) + 1
        board_row2.pop(ind)
        board_row2.insert(ind, move)

    if x == '2':
        ind = int(y) + 1
        board_row3.pop(ind)
        board_row3.insert(ind, move)

    print(' '.join(map(str, board_row0)))
    print(' '.join(map(str, board_row1)))
    print(' '.join(map(str, board_row2)))
    print(' '.join(map(str, board_row3)))
    print('\n')
    return board_row1, board_row2, board_row3


def check_winner():
    while True:

        if ('X' in board_row1[1] and 'X' in board_row1[2] and 'X' in board_row1[3]) or (
                'X' in board_row2[1] and 'X' in board_row2[2] and 'X' in board_row2[3]) or (
                'X' in board_row3[1] and 'X' in board_row3[2] and 'X' in board_row3[3]) or (
                'X' in board_row1[1] and 'X' in board_row2[1] and 'X' in board_row3[1]) or (
                'X' in board_row1[2] and 'X' in board_row2[2] and 'X' in board_row3[2]) or (
                'X' in board_row1[3] and 'X' in board_row2[3] and 'X' in board_row3[3]) or (
                'X' in board_row1[1] and 'X' in board_row2[2] and 'X' in board_row3[3]) or (
                'X' in board_row1[3] and 'X' in board_row2[2] and 'X' in board_row3[1]):
            print("Победили 'крестики' ")
            print("Игра завершена")
            return True

        if ('O' in board_row1[1] and 'O' in board_row1[2] and 'O' in board_row1[3]) or (
                'O' in board_row2[1] and 'O' in board_row2[2] and 'O' in board_row2[3]) or (
                'O' in board_row3[1] and 'O' in board_row3[2] and 'O' in board_row3[3]) or (
                'O' in board_row1[1] and 'O' in board_row2[1] and 'O' in board_row3[1]) or (
                'O' in board_row1[2] and 'O' in board_row2[2] and 'O' in board_row3[2]) or (
                'O' in board_row1[3] and 'O' in board_row2[3] and 'O' in board_row3[3]) or (
                'O' in board_row1[1] and 'O' in board_row2[2] and 'O' in board_row3[3]) or (
                'O' in board_row1[3] and 'O' in board_row2[2] and 'O' in board_row3[1]):
            print("Победили 'нолики' ")
            print("Игра завершена")
            return True

        else:
            return False


def start_game():
    while ("-" in board_row1 or "-" in board_row2 or "-" in board_row3):
        if check_winner() is not True:
            choose_and_check_position()
            choose_x_or_o()
            place_x_or_o()
        else:
            break

    if ("-" not in board_row1 and "-" not in board_row2 and "-" not in board_row3):
        print('Ничья!')
        print("Игра завершена")

start_game()