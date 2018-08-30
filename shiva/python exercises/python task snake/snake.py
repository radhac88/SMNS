import random

pos = [0, 0, 0, 0]
names = []
snakes = {17: 7, 54: 20, 62: 43, 64: 4, 87: 63, 93: 73, 96: 21, 99: 21}
ladders = {4: 10, 9: 22, 20: 38, 28: 56, 40: 19, 51: 16, 63: 18, 71: 20}


def numofplayers():
    k = 0
    while k < 1:
        numofplayers = int(input("enter number of players: "))
        if numofplayers < 2:
            print("please enter a value between 2-4 ")
        elif numofplayers > 4:
            print("please enter number which is less than '5' ")
        else:
            k += 1
    print("no of players : ", numofplayers)
    return numofplayers


num = numofplayers()


def diceroll():
    d = random.randint(1, 6)
    return d


def players():
    for i in range(0, num):  # num is used here
        print('player', i + 1, 'input your name')
        name = input("\n")
        print('welcome', name)
        names.append(name)
    print('\nplayers:')
    for i in names:
        print(i)

    print('\n')


players_pos = {}


def assign():
    for i in names:
        x = names.index(i)
        players_pos[i] = pos[x]


def move():
    q = 0
    while q < 1:
        for i in names:
            y = diceroll()
            z = pos[names.index(i)]
            print("\n")
            input("player : ")
            print(i)
            print("current pos", z)
            input("roll a die")
            print("dice rolled = ", y)
            w = y + z
            pos[names.index(i)] = w
            print("players position after rolling ", w)
            if pos[names.index(i)] == 100:
                q += 2
            elif pos[names.index(i)] > 100:
                q += 2
            if q > 1:
                break

            for a in snakes:
                if a == pos[names.index(i)]:
                    print('unlucky, you hit a snake! ', i)
                    print('the snake is', snakes[a], 'long')
                    print('you go down', snakes[a], 'places')
                    pos[names.index(i)] -= snakes[a]
                    print('you are now on', pos[names.index(i)])
                    print("\n")
            for a in ladders:
                if a == pos[names.index(i)]:
                    print("very nice, you re on a ladder! ", i)
                    print('the ladder is', ladders[a], 'long')
                    print('you go up', ladders[a], 'places')
                    pos[names.index(i)] += ladders[a]
                    print('you are now on', pos[names.index(i)])
                    print("\n")
    return i


def main():
    players()
    assign()
    winner = move()
    print("********************\nwinner :{0} \n********************".format(winner))


main()
