import random

def hangman(word):
    wrong=0
    stages = ["",
            "|______    ",
            "|          ",
            "|          ",
            "|     |    ",
            "|     o    ",
            "|   / | \  ",
            "|    / \   ",
            "|          ",
            "|          "]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("ハングマンへようこそ")
    print(" ".join(board))

    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想して"
        char=input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong += 1
        print(wrong)
        wrong += 1

        print((" ".join(board)))
        e=wrong + 1
        print("\n".join(stages[0: e]))

        if "_"not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("あなたの負け！正解は{}.".format(word))


answer =["suto6","cod","mario","apex"]
r = random.randint(0,len(answer)-1)
hangman(answer[r])
