import random

def dice():
    randvalue=random.randint(1,6)
    return randvalue

playlist=(a1,a2,a3,a4,b1,b2,b3,b4)
def win(player1,player2):
    if player1==56:
        print("so, congragulations player1. you won")
    elif player2==56:
        print("so, congragulations player2. you won")


player1=0
player2=0
currentplayer=-1;



for r in range(15):
    for c in range(15):
        if (r==6 and c>=6 and c<9) or (r==7 and c>=6 and c<9) or (r==8 and c>=6 and c<9)   :
            print(" ",end="   ")
        elif r==6 or r==7 or r==8:
            print(0,end="   ")
        elif c==6 or c==7 or c==8:
            print(0,end="   ")
        else:
            print(" ",end="   ")
    print("\n")

