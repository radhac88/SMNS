import random

def dice():
	randvalue=random.randint(1,6)
	return randvalue




snakes={3:24,14:42,30:86,37:57,50:96,66:74};

ladders={95:18,77:45,60:28,34:10,20:2};


player1=0
player2=0
curplayer=-1;

def win(p1,p2):
	p1=player1;
	p2=player2;
	if player1==100:
		print("player1 won")
	elif player2==100:
		print("player2 won")

while(player1<100 and player2<100):
	if curplayer==-1:
		print("Player1 Turn")
		input1=input("enter r to throw the dice")
		if input1=='r':
			x=dice()
			print(str(x)+"random number")
		pos=player1+x;	
		if pos<=100:
			#for pos in snakes:
			#	x=snakes[pos]
			player1=player1+x;
		print("player1 is in"+str(player1))
		win(player1,player2)	
		curplayer=-2
	elif curplayer==-2:
		print("Player2 Turn")
		input1=input("enter r to throw the dice")
		if input1=='r':
			x=dice()
			print(str(x)+"random number")
		player2=player2+x;
		print("player2 is in"+str(player2))
		win(player1,player2)	
		curplayer=-1



