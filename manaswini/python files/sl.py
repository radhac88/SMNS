import random
player1=0;
player2=0;
ladder={3:17,
		 20:33,
		 28:42,
		 40:46,
		 47:60,

}
snake={ 25:11,
		 32:16,
		 48:34,
		 58:45,
		 60:47,
}


while(player1<100):
	print("player 1")
	print(input("hit enter to roll the dice"));
	dice=random.randint(1,6)
	print(dice)
	if player1+dice<=100:
			player1=player1+dice;
	if player1 in ladder:
		print("its a ladder!!")
		player1=ladder[player1]
	elif player1 in snake:
		print("caught by snake!!")
		player1=snake[player1]
	elif player1==100:
		print("player1 won!")
		break
	print("player1 is now at",player1)
	print("player 2")
	print(input("hit enter to roll the dice"));
	dice=random.randint(1,6)
	print(dice)
	if player2+dice<=100:
			player2=player2+dice;
	if player2 in ladder:
		print("its a ladder!!")
		player2=ladder[player2]
	elif player2 in snake:
		print("caught by snake!!")
		player2=snake[player2]
	elif player2 == 100:
		print("player2 won!")
		break
	print("player2 is now at",player2)
	print("_____________________________________")



		
