def printBoard(xState, oState):
    zero = 'X'if xState[0] else('O'if oState[0] else " ")
    one = 'X'if xState[1] else('O'if oState[1] else " ")
    two = 'X'if xState[2] else('O'if oState[2] else " ")
    three = 'X'if xState[3] else('O'if oState[3] else " ")
    four = 'X'if xState[4] else('O'if oState[4] else " ")
    five = 'X'if xState[5] else('O'if oState[5] else " ")
    six = 'X'if xState[6] else('O'if oState[6] else " ")
    seven = 'X'if xState[7] else('O'if oState[7] else " ")
    eight = 'X'if xState[8] else('O'if oState[8] else " ")
    print('\n')
    print(f"  {zero}  |  {one}  |  {two}")
    print(f" --- | --- | ---")
    print(f"  {three}  |  {four}  |  {five}")
    print(f" --- | --- | ---")
    print(f"  {six}  |  {seven}  |  {eight}")
    print('\n')


def sum(a, b, c):
    return a+b+c


def playerWin(xState, oState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("\n_______ X WON _______\n")
            return 1
        if(sum(oState[win[0]], oState[win[1]], oState[win[2]]) == 3):
            print("\n_______ O WON _______\n")
            return 0
    return -1


if __name__ == "__main__":

        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        oState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1  # 1 for x 0 for O
        print("Welcome")
        temp2=1
        while temp2==1:
            printBoard(xState, oState)
            if (turn == 1):
                print("X`s Turn.")
                value = int(input("Enter the position for X : "))
                if(value == 7 or value == 8 or value == 9):
                    xState[value-7] = 1
                elif(value == 1 or value == 2 or value == 3):
                    xState[value+5] = 1
                else:
                    xState[value-1] = 1
            else:
                print("O`s Turn.")
                value = int(input("Enter the position for O : "))
                if(value == 7 or value == 8 or value == 9):
                    oState[value-7] = 1
                elif(value == 1 or value == 2 or value == 3):
                    oState[value+5] = 1
                else:
                    oState[value-1] = 1
            won = playerWin(xState, oState)
            if(won != -1):
                print("WINING STATE")
                printBoard(xState, oState)
                print("\n______GAME OVER________\n\n")
                print("1.PLAY AGAIN\n")
                print("2.EXIT (ctrl + c)\n")
                choice=int(input("Enter choice: "))
                if(choice==1):
                    temp2==2
                break
            turn = 1-turn
# play with
#     ("  7  |  8  |  9 ")
#     (" --- | --- | ---")
#     ("  4  |  5  |  6 ")
#     (" --- | --- | ---")
#     ("  1  |  2  |  3 ")
# respective num keys for respective positions
