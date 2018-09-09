# from codegen import getCode 
import random
colors = ['R','O','Y','G','P','W']
from clear import clear

def getCode():
    # orange, red, white, green, yellow, purple
    # ORWGYP
    # ROYGPW
    # goal is to generate random code of 4 colors
    i = 0
    code = []
    while i < 4:
        x = random.randint(0,5)
        color = colors[x]
        # print(color)
        code.append(color)
        i += 1
    # print(code)
    return code

def startGame():
    print("Welcome to Mastermind!")
    print()
    print("Adapted and coded by McKennah and Gavin")
    print()
    go = input("Are you ready to play? [Y/N]").upper()
    if go == 'Y':
        print("Let's play!")
        code = getCode()
        print("The secret code has been generated!\nLet's see if you can figure it out!\n")

        play(code)
    else:
        print("Ok, maybe another time then.")
        return 

def play(code):
    # initialize variables
    win = False
    guesses = []
    # codelist = list(code)

    # build game board
    for i in range(0,10):
        guesses.append([i+1,'----',0,0])
    
    # start turns
    print("Time to guess! You must choose from the following colors. R,O,Y,G,W,P")
    for i in range(0,10):
        # assign guess to list position for this turn
        guesses[i][1] = getGuess()
        
        # check guess?
        # check for 'Red' pegs = where color and location are correct
        r = [] # red pegs
        w = 0 # white pegs
        g = list(guesses[i][1].upper()) # guess
        wgl = list(g) # white guess list to be used for white pegs
        wcl = list(code) # white code list 
        # print("g: " + str(len(g)))
        # print("code: " + str(len(code)))
        # print("wgl: " + str(len(wgl)))
        # print("wcl: " + str(len(wcl)))
        # print(code, guesses[i][1].upper())
        for j in range(3,-1,-1):
            # print(j, g[j], code[j])
            if g[j] == code[j]:
                r.append(1)

                wgl.pop(j)
                wcl.pop(j)
            else:
                r.append(0)
        
        guesses[i][2] = sum(r)
        # print("R: " + str(guesses[i][2]))
        # print("wgl", "".join(wgl))
        # print("wcl", "".join(wcl))

        # white pegs - look at those not matched exactly and check to see if they exist and how many.
        if len(wgl) > 0:
            for k in set(wgl):
                w += "".join(wcl).count(k)
        guesses[i][3] = w   

        # if guess is correct 
        if sum(r) == 4:
            win = True
            break

        # print game board
        # print(code)
        clear()
        print('Turn\tGuess\tRed\tWhite')   
        for x in guesses[::-1]:
            print("%i\t%s\t%i\t%i" % (x[0], x[1], x[2], x[3]))
    
    # print("this is the play function returning the valid guess: " +guess)
    if win:
        print("Congratulations!\nYou correctly guess the secret code!\nCode:", "".join(code))
    return

def getGuess():
    i = 0
    while i < 2:
        # print("\tstart loop")
        i = 0    
        charcount = 0
        # print("\tstart i = " , str(i)) 
        guess = input("Enter your guess: ").upper()
        # Check the length
        while len(guess) != 4:
            guess = input("Your guess must be exactly 4 characters!\nTry again: ").upper()
        i += 1 # guess is the right length    
        # print("\tlength check i = " , str(i))       
        # Check the characters
        chars = list(guess)
        for char in chars:
            if char in colors:
                charcount += 1
            else: 
                print(char + " is not a valid color!")
        # print("\tpre-char check i = " , str(i))                    
        if charcount == 4:
            i += 1 # characters are valid
        # print("\tchar check i = " , str(i))    
        continue

    # print("Your guess is " + guess)
    return guess
