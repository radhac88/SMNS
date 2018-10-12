import random

def dice():
    randvalue=random.randint(1,6)
    return randvalue

pos={1:(1,8),2:(2,8),3:(3,8),4:(4,8),5:(5,8),6:(6,9),7:(6,10),8:(6,11),9:(6,12),10:(6,13),11:(6,14),12:(7,14),13:(8,14),14:(8,13),15:(8,12),16:(8,11),17:(8,10),18:(8,9),19:(9,8),20:(10,8),21:(11,8),22:(12,8),23:(13,8),24:(14,8),25:(14,7),26:(14,6),27:(13,6),28:(12,6),29:(11,6),30:(10,6),31:(9,6),32:(8,5),33:(8,4),34:(8,3),35:(8,2),36:(8,1),37:(8,0),38:(7,0),39:(6,0),40:(6,1),41:(6,2),42:(6,3),43:(6,4),44:(6,5),45:(5,6),46:(4,6),47:(3,6),48:(2,6),49:(1,6),50:(0,6),51:(0,7),52:(1,7),53:(2,7),54:(3,7),55:(4,7),56:(5,7)}
pos1={1:(13,6),2:(12,6),3:(11,6),4:(10,6),5:(9,6),6:(8,5),7:(8,4),8:(8,3),9:(8,2),10:(8,1),11:(8,0),12:(7,0),13:(6,0),14:(6,1),15:(6,2),16:(6,3),17:(6,4),18:(6,5),19:(5,6),20:(4,6),21:(3,6),22:(2,6),23:(1,6),24:(0,6),25:(0,7),26:(0,8),27:(1,8),28:(2,8),29:(3,8),30:(4,8),31:(5,8),32:(6,9),33:(6,10),34:(6,11),35:(6,12),36:(6,13),37:(6,14),38:(7,14),39:(8,14),40:(8,13),41:(8,12),42:(8,11),43:(8,10),44:(8,9),45:(9,8),46:(10,8),47:(11,8),48:(12,8),49:(13,8),50:(14,8),51:(14,7),52:(13,7),53:(12,7),54:(11,7),55:(10,7),56:(9,7)}
def grid(a11,a12,a21,a22,a31,a32,a41,a42,b11,b12,b21,b22,b31,b32,b41,b42):
    for r in range(15):
        for c in range(15):
            if r==a11 and c==a12:
                print("a1",end="  ")
            elif r==a21 and c==a22:
                print("a2",end="  ")
            elif r==a31 and c==a32:
                print("a3",end="  ")
            elif r==a41 and c==a42:
                print("a4",end="  ")
            elif r==b11 and c==b12:
                print("b1",end="  ")
            elif r==b21 and c==b22:
                print("b2",end="  ")
            elif r==b31 and c==b32:
                print("b3",end="  ")
            elif r==b41 and c==b42:
                print("b4",end="  ")
            elif (r==6 and c>=6 and c<9) or (r==7 and c>=6 and c<9) or (r==8 and c>=6 and c<9):
                print(" ",end="   ")
            elif r==6 or r==7 or r==8:
                print(0,end="   ")
            elif c==6 or c==7 or c==8:
                print(0,end="   ")
            else:
                print(" ",end="   ")
        print("\n")


def position(a1,a2,a3,a4,b1,b2,b3,b4):
        if(a1>0):
            x=pos[a1]
            x1=list(x)
        else: x1=[-1,-1]
        list1=(a2,a3,a4)
        list2=(b1,b2,b3,b4)
        for z in list1:
            if(z>0):
                y=pos[z]
                x1.append(y[0])
                x1.append(y[1])
            else: 
                x1.append(-1)
                x1.append(-1)
        for z in list2:
            if(z>0):
                y=pos1[z]
                x1.append(y[0])
                x1.append(y[1])
            else: 
                x1.append(-1)
                x1.append(-1)
        grid(*x1)
       
def win(a1,a2,a3,a4,b1,b2,b3,b4):
    if a1==57 and a2==57 and a3==57 and a4==57:
        print("so, congragulations player1. you won")
    elif b1==57 and a2==57 and a3==57 and a4==57:
        print("so, congragulations player2. you won")

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
        position(a1,a2,a3,a4,b1,b2,b3,b4)
        win(a1,a2,a3,a4,b1,b2,b3,b4)  

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

        while(b1>=1 or b2>=1 or b3>=1 or b4>=1) and r==0 and f!=0:
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
        print("b1 is at",b1,"\nb2 is at",b2,"\nb3 is at",b3,"\nb4 is at",b4)
        print("*********************************")
        curplayer=-1
        position(a1,a2,a3,a4,b1,b2,b3,b4)
        win(a1,a2,a3,a4,b1,b2,b3,b4)







