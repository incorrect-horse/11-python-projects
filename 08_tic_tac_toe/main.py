import os


def clear_screen():
    os.system("clear")


def game_reference():
    grid = "#################\n"\
"#  GRID # REFS  #\n"\
"# | 1 | 2 | 3 | #\n"\
"# | 4 | 5 | 6 | #\n"\
"# | 7 | 8 | 9 | #\n"\
"#               #\n"\
"#################"

    print(f"\n{grid}")


def print_board():
    game_reference()

    row1 = f"\n  |{board[0]}|{board[1]}|{board[2]}|"
    row2 = f"  |{board[3]}|{board[4]}|{board[5]}|"
    row3 = f"  |{board[6]}|{board[7]}|{board[8]}|"

    print(row1)
    print(row2)
    print(row3)


def player_move(icon):
    if icon == "X":
        player = 1
    elif icon == "O":
        player = 2
    
    print(f"\nYour turn, player {player}.")

    choice = int(input("Enter your move (1-9): ").strip())

    if choice -1 in range(9):
        if board[choice - 1] == "   ":
            board[choice - 1] = f" {icon} "
        else:
            print(f"\nThat space is taken!")
            player_move(icon)
    else:
        print(f"\nNumber not valid, try again.")
        player_move(icon)


def is_victory(icon):
    icon = " " + icon + " "
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_draw():
    if "   " not in board:
        return True
    else:
        return False


board = ["   " for i in range(9)]

try:
    while True:
        clear_screen()
        print_board()
        player_move("X")

        clear_screen()
        print_board()

        if is_victory("X"):
            print(f"\nX Wins! Congratualtions!")
            break
        elif is_draw():
            print("\nIt's a draw...")
            break

        player_move("O")
        if is_victory("O"):
            clear_screen()
            print_board()
            print(f"\nO Wins! Congratualtions!")
            break
        elif is_draw():
            print("\nIt's a draw...")
            break
except ValueError:
    # if user enters invalid input to prompt
    pass
except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("\nGoodbye!")
