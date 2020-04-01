import math
from random import randint
import time
print('------------------------')
print('Multiplcation Practice!')
print('For Annie from Uncle Gaelen')
print('-----------------------')

def execute_game():
    numq = input('How many questions do you want to do? (Type in how many and press enter)')
    try:
        int(numq)
    except:
        print('Enter a number please!')
        execute_game()
    N1 = [randint(0,10) for n in range(0,int(numq))]
    N2 = [randint(0,10) for n in range(0,int(numq))]
    start = input('Ok! Press Enter to start!')
    stime = time.time()

    corr_count = 0

    for i in range(0,int(numq)):
        a = input(str(N1[i]) +' X ' + str(N2[i])+ ' = ')
        try:
            if int(a) == N1[i]*N2[i]:
                print('Correct!')
                corr_count = corr_count + 1
            else:
                print('Incorrect! The correct answer is '+ str(N1[i]*N2[i]))
        except:
            print('Incorrect! The correct answer is '+ str(N1[i]*N2[i]))
    etime = time.time()

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

    print('Your time was ' + str(int(etime-stime))+ ' seconds!')

    rate = (etime-stime)/float(numq)
    if rate > 6:
        print('You could be faster!')
    if rate < 3:
        print('You are sooooo fast!')
    else:
        print('You are pretty fast!')
    rep = input('Do you want to play again? Type y or n and press enter')
    if rep == 'y':
        execute_game()
    else:
        return

execute_game()
