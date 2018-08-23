player1=0
player2=0
numbers = [i for i in range(1,101)]
numbers = numbers[::-1]
levels = [i for i in numbers[::-10]]
is_reversed = False

for level in levels:

    if is_reversed:
        for number in reversed(numbers[level-1:level+9]):
        	if number==player1:
				print("p1")
			else:	
            	print('{:4}'.format(number), end='|')
         
    else:
        for number in numbers [level-1:level+9]:
            print('{:4}'.format(number), end='|')  

          
        

    

    is_reversed = not is_reversed
    print()	
def snake_ladder(n):
	ladders = {1:38,4:14,9:31,21:42,28:84,36:44,51:67,71:91,80:100}
	snakes = {98:78,95:75,93:73,87:24,64:60,62:19,56:53,49:11,48:26,16:6}
	
	if n in ladders:
		print("its a ladder climb up!")
		n=ladders[n]
		return n
	elif n in snakes:
		print("its a snake climb down!!")
		n=snakes[n]
		return n
	else:
		return n		
import random
min=1
max=6
def roll_dice(r):
	d=random.randint(min,max)
	print("the value of dice is:",d)
	d=r+d
	return d
while(player1<100 and player2<100):
	print("its turnns of player1")
	input1=input("enter any key" )
	player1=roll_dice(player1)
	player1=snake_ladder(player1)
	print("Current status of Player1:",player1)
	
	if player1>99:
		print("player1 won")
		break
	print("its turns of player2")	
	input1=input("enter any key" )		
	player2=roll_dice(player2)
	player2=snake_ladder(player2)
	print("Current status of player2:",player2)	
	if player2>99:
		print("player2 won!")
	
	
	
		
		
			
		


	



	
