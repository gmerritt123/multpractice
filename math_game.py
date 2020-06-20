import math
from random import randint, choice
import time
import sys
print('------------------------')
print('Math Practice!')
print('For Annie from Uncle Gaelen')
print('-----------------------')

def init():
    game = input('What game do you want to play? (Type number and press enter to select)\n 1) Multiplication\n 2) Addition\n 3) Subtraction\n 4) Division\n 5) Random!')
    try:
        if int(game) > 5:
            print('Please enter a number between 1 and 5!')
            print(game)
            init()
    except:
        print('Please enter a number between 1 and 5!')
        print(game)
        init()
    numq = input('How many questions do you want to do? (Type in how many and press enter)')
    try:
        int(numq)
    except:
        print('Enter a number please!')
        init()
    print('ok, ' +numq+ ' questions')
    execute_game(int(game),int(numq))
    
def execute_game(g,nq):
    N1 = [randint(1,10) for n in range(0,nq)]
    N2 = [randint(0,10) for n in range(0,nq)]
    start = input('Ok! Press Enter to start!')
    stime = time.time()
    
    corr_count = 0
    dg = False
    for i in range(0,len(N1)):
        corr = False
        if g == 5:
            dg = True
            g = choice([1,2,3,4])
        if g == 1:
            corr = mult_game(N1[i],N2[i])
        elif g == 2:
            corr = add_game(N1[i],N2[i])
        elif g == 3:
            corr = sub_game(N1[i],N2[i])
        elif g == 4:
            corr = div_game(N1[i],N2[i])

        if dg == True:
            g = 5

        if corr == True:
            corr_count = corr_count + 1

    etime = time.time()
    end_game(corr_count,nq,stime,etime)

def mult_game(n1,n2):
    corr = False
    a = input(str(n1) +' X ' + str(n2)+ ' = ')
    try:
        if int(a) == n1*n2:
            print('Correct!')
            corr = True
        else:
            print('Incorrect! The correct answer is '+ str(n1*n2))
    except:
        print('Incorrect! The correct answer is '+ str(n1*n2))
    return corr

def add_game(n1,n2):
    corr = False
    a = input(str(n1) +' + ' + str(n2)+ ' = ')
    try:
        if int(a) == n1+n2:
            print('Correct!')
            corr = True
        else:
            print('Incorrect! The correct answer is '+ str(n1+n2))
    except:
        print('Incorrect! The correct answer is '+ str(n1+n2))
    return corr

def sub_game(n1,n2):
    corr = False
    nf = max(n1,n2)
    nl = min(n1,n2)
    a = input(str(nf) +' - ' + str(nl)+ ' = ')
    try:
        if int(a) == nf-nl:
            print('Correct!')
            corr = True
        else:
            print('Incorrect! The correct answer is '+ str(nf-nl))
    except:
        print('Incorrect! The correct answer is '+ str(nf-nl))
    return corr

def div_game(n1,n2):
    if n1 == 0:
      n1 = randint(1,10)
    corr = False
    a = input(str(n1*n2) +' / ' + str(n1)+ ' = ')
    try:
        if int(a) == n2:
            print('Correct!')
            corr = True
        else:
            print('Incorrect! The correct answer is '+ str(n2))
    except:
        print('Incorrect! The correct answer is '+ str(n2))
    return corr
    
def end_game(corr_count,numq,stime,etime):
    print('Game Complete!')
    print('You got ' + str(corr_count)+ ' correct out of '+str(numq)+'!')
    grade = float(corr_count)/float(numq)
    if grade > 0.9:
        print('Your grade: A+! :-D')
    elif grade >0.8:
        print('Your grade: A! :-D')
    elif grade >0.7:
        print('Your grade: B! :-)')
    elif grade >0.6:
        print('Your grade: C! :-/')
    elif grade >0.5:
        print('Your grade: D! :-(')
    else:
        print('Your grade: F! :-(')

    print('Your time was ' + str(round(etime-stime,2))+ ' seconds!')

    rate = (etime-stime)/float(numq)
    if rate > 6:
        print('You could be faster!')
    if rate < 3:
        print('You are sooooo fast!')
    else:
        print('You are pretty fast!')
    rep = input('Do you want to play again? Type y or n and press enter')
    if rep == 'y':
        init()
    else:
        print('Closing!')
        sys.exit()

init()
