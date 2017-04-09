#Introduction to Programming
#Noughts_And_Crosses_01.py
#Student Name: Rafia Bushra
#Student ID: 268449

def main():

    board = [[".", ".", "."],
             [".", ".", "."],
             [".", ".", "."]]
    for c in range(3):
        for r in range(3):
            print(board[r][c], end = "")
        print()
    
    turns = 0

    while turns < 9:
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

        except ValueError:
            print("Error: enter two integers, separated with spaces.")

        except IndexError:
            print("Error: coordinates must be between 0 and 2.")


main()
