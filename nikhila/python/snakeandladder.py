import random

def dice():
	randvalue=random.randint(1,6)
	return randvalue

def box(p1,p2):
	for a in range(100,1,-20):
		for b in range(a,a-10,-1):
			if b==p1 and b==p2:
				print("p1p2",end=" ")
			elif b==p1:
				print("p1",end=" ")
			elif b==p2:
				print("p2",end=" ")
			else:
				print('%3d' %b,end=" ")
		print("\n")	
		for b in range(a-19,a-9):
			if b==p1 and b==p2:
				print("p1p2",end=" ")
			elif b==p1:
				print("p1",end=" ")
			elif b==p2:
				print("p2",end=" ")
			else:
				print('%3d' %b,end=" ")
		print("\n")		


ladders={3:24,14:42,30:86,37:57,50:96,66:74}

snakes={95:18,77:45,60:28,34:10,20:2}


player1=0
player2=0
currentplayer=-1;

def win(player1,player2):
	if player1==100:
		print("so, congragulations player1. you won")
	elif player2==100:
		print("so, congragulations player2. you won")

while(player1<100 and player2<100):
	if currentplayer==-1:
		print("Player1 Turn")
		input1= input("press enter to the roll dice")
		if input1=='':
			x=dice()
			print("dice rolled :"+str(x))
		if player1+x<=100:
			player1=player1+x;
			if player1 in snakes:
				player1=snakes[player1]
				print("Opps!you have bitten by snake..")
			elif player1 in ladders:
				player1=ladders[player1]
				print("Hurray!you got ladder..")
		print("player1 is at "+str(player1))
		print("player2 is at "+str(player2)+"\n")
		box(player1,player2);
		print("\n**************************")
		win(player1,player2)	
		currentplayer=-2
	elif currentplayer==-2:
		print("Player2 Turn")
		input1=input("press enter to roll dice")
		if input1=='':
			x=dice()
			print("dice rolled :"+str(x))	
		if player2+x<=100:
			player2=player2+x;
			if player2 in snakes.keys():
				player2=snakes[player2]
				print("Opps!you got bitten by snake..")
			elif player2 in ladders.keys():
				player2=ladders[player2]
				print("Hurray!you got ladder..")
		print("player2 is at "+str(player2))
		print("player1 is at "+str(player1)+"\n")
		box(player1,player2);
		print("**************************")
		win(player1,player2)	
		currentplayer=-1



