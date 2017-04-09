# Introduction to Programming
# Noughts_And_Crosses_01.py
# Student Name: Rafia Bushra
# Student ID: 268449

def main():
    board = [[".", ".", "."],
             [".", ".", "."],
             [".", ".", "."]]
    for c in range(3):
        for r in range(3):
            print(board[r][c], end="")
        print()

    turns = 0

    while True:
        if turns % 2 == 0:
            mark = "X"
        else:
            mark = "O"
        coordinates = input("Player " + mark + ", give coordinates: ")

        try:
            x, y = coordinates.split(" ")
            x = int(x)
            y = int(y)

            if board[x][y] != ".":
                print("Error: a mark has already been placed on this square.")
                continue
            else:
                board[x][y] = mark
                turns += 1
                for c in range(3):
                    for r in range(3):
                        print(board[r][c], end="")
                    print()

            if (board[x][0] == board[x][1] == board[x][2] == mark) or \
                (board[0][y] == board[1][y] == board[2][y] == mark):
                print("The game ended, the winner is", mark)
                break
            elif (board[0][0] == board[1][1] == board[2][2] == mark) or \
                (board[0][2] == board[1][1] == board[2][0] == mark):
                print("The game ended, the winner is", mark)
                break
            elif turns == 9:
                print("Draw!")
                break


        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")


main()
