import random

def dice():
    randvalue=random.randint(1,6)
    return randvalue



def grid():
    for r in range(15):
        for c in range(15):
            if (r==6 and c>=6 and c<9) or (r==7 and c>=6 and c<9) or (r==8 and c>=6 and c<9):
                print(" ",end="   ")
            elif r==6 or r==7 or r==8:
                print(0,end="   ")
            elif c==6 or c==7 or c==8:
                print(0,end="   ")
            else:
                print(" ",end="   ")
        print("\n")

a1=-1
a2=-1
a3=-1
a4=-1
b1=-1
b2=-1
b3=-1
b4=-1
curplayer=-1
while(a1<56 and a2<56 and a3<56 and a4<56 and b1<56 and b2<56 and b3<56 and b4<56):
    if(curplayer==-1):
        print("player1s turn");
        input1= input("press enter to the roll dice")
        if input1=='':
            x=dice()
            print("dice rolled :"+str(x))

        if x==6 and a1==-1:
            a1=1
            f=0
            print("coin a1 will be on the board")
        elif x==6 and a2==-1:
            a2=1
            f=0
            print("coin a2 will be on the board")
        elif x==6 and a3==-1:
            a3=1
            f=0
            print("coin a3 will be on the board")
        elif x==6 and a4==-1:
            a4=1
            f=0
            print("coin a4 will be on the board")

        r=0;
        while (a1>=1 or a2>=1 or a3>=1 or a4>=1) and r==0 and f!=0:
            coin=int(input("which coin you want to move 1/2/3/4"))
            if(coin==1 and a1>=1):
                a1=a1+x
                r=-1
            elif(coin==2 and a2>=1):
                a2=a2+x
                r=-1
            elif(coin==3 and a3>=1):
                a3=a3+x
                r=-1
            elif(coin==4 and a3>=1):
                a4=a4+x
                r=-1
            else:
                print("choose right coin")
                r=0
        f=1    
        print("a1 is at",a1)
        print("a2 is at",a2)
        print("a3 is at",a3)
        print("a4 is at",a4)
        print("*********************************")
        curplayer=-2  
        grid()


    elif(curplayer==-2):
        print("player2s turn")
        input1= input("press enter to the roll dice")
        if input1=='':
            x=dice()
            print("dice rolled :"+str(x))

        if x==6 and b1==-1:
            b1=1
            f=0
            print("coin b1 will be on to the board")
        elif x==6 and b2==-1:
            b2=1
            f=0
            print("coin b2 will be on to the board")
        elif x==6 and b3==-1:
            b3=1
            f=0
            print("coin b3 will be on to the board")
        elif x==6 and b4==-1:
            b4=1
            f=0
            print("coin b4 will be on to the board")

        if (b1>=1 or b2>=1 or b3>=1 or b4>=1) and r==0 and f!=0:
            coin=int(input("which coin you want to move 1/2/3/4"))
            if(coin==1 and b1>=1):
                b1=b1+x  
                r=-1  
            elif(coin==2 and b2>=1):
                b2=b2+x
                r=-1
            elif(coin==3 and b3>=1):
                b3=b3+x
                r=-1
            elif(coin==4 and b3>=1):
                b4=b4+x
                r=-1
            else:
                print("choose right coin")
                r=0
            f=1    
        print("b1 is at",b1)
        print("b2 is at",b2)
        print("b3 is at",b3)
        print("b4 is at",b4)
        print("*********************************")
        curplayer=-1



def win(player1,player2):
    if player1==56:
        print("so, congragulations player1. you won")
    elif player2==56:
        print("so, congragulations player2. you won")





