import random
import math

def printword(pword):
    s = ''
    for c in pword:
        s = s + c
        s = s + ' '
    return s

def findletter():
    global pword
    global missedletters
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                pword = pword[0:i] + word[i] + pword[i+1:len(word)]
    elif letter not in missedletters:
        missedletters.append(letter)

def draw_hangman(m):
    print(10 * '_')
    print('|', 6 * ' ', '|')

    print('|', 5*' ', end = ' ')
    if m > 0:
        print('( )')
    else:
        print()
    
    print('|', 4*' ', end = ' ')
    if m > 3:
        print('__|__')
    elif m > 2:
        print('__|')
    elif m > 1:
        print('  |')
    else:
        print()

    print('|', 6*' ', end = ' ')
    if m > 1:
        print('|')
    else:
        print()

    print('|', 5*' ', end = ' ')
    if m > 5:
        print('/ \ ')
    elif m > 4:
        print('/')
    else:
        print()
    
    print('|', 4*' ', end = ' ')
    if m > 5:
        print('/   \ ')
    elif m > 4:
        print('/')
    else:
        print()

def score_calculator(length, pword):
    if length < 7:
    	return 100 - 7.5 * length
    s = 0
    for c in pword:
    	if c != '_' and c != ' ':
    		s += 2.5
    return s




print('Hello! Welcome to Hangman!')

wdb = [] # words database
answer = '1'
while answer == '1':
    print('Press 0 if you want to play against the computer')
    print('Press 1 if you want to play against a human')
    choice = int(input())

    if choice == 1:
        word = input('Pick a word (If you type greek, please write in capitals)\n').upper() #xoris tonous
    elif choice == 0:
        myfile = open("wordsdb.txt", "r")
        if len(wdb) == 0:
            for newword in myfile:
                wdb.append(newword)
        r = math.floor(random.random()*len(wdb))
        word = wdb[r].upper()
        word = word[0:len(word)-1]
        myfile.close()
    pword = word[0] + (len(word)-1)*'_' # printed word

    r = random.random()
    if r < 0.5:
        letter = word[0]
        findletter()

    missedletters = []
    while True:
        for i in range(50):
            print()
        draw_hangman(len(missedletters))
        print()
    #    print(word)
        print(printword(pword))

        if len(missedletters) != 0:
            print(missedletters[0], end = ' ')
            for i in missedletters[1:len(missedletters)]:
                print(', ', i, end = ' ')

        letter = input('\nType a letter\n').upper()
        findletter()
        if pword == word:
            print('YOU WON')
            print('Your score was ', score_calculator(len(missedletters), pword), '/ 100')
            break
        if len(missedletters) >= 7:
            print('YOU LOSE...')
            print('The word was ', word)
            print('Your score was ', score_calculator(len(missedletters), pword), '/ 100')
            break
    answer = input('Press 1 to play again\n')
    for i in range(50):
        print()
