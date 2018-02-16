'''                         Guess_My_Number
Overview ->
The computer randomly generates a number. The user inputs a number, and the
computer will tell you if you are too high, or too low. Then you will get 
to keep guessing until you guess the number.
What we will be Using in the code:
Random, Integers, Input/Output, Print, While (Loop), If/Elif/Else
'''    
from random import randint
import os
import time
import sys

def load_program():
    os.system('cls')
    print ("\t\tProgram Is Loading/Storing Files")
    print ("\t\t\t",end="")
    for i in range(0,4):
        print ("o o ",end="")
        time.sleep(1)
    print ("")
        
def start_game(key):
    print ("Hello There ! What's your Name -> ",end="")
    player_name=input().upper()
    print ("Well, ",player_name," I had already decided the number ",end="")
    print ("as per your sack choice.")
    print ("Let us Start the Game ... ",end="")
    print ("Keep on guessing the number in atmost 10 trails !!!")   
    flag=0    
    for trial in range(0,10):
        print ("Take a guess - > ",end="")
        guess=int(input())
        if guess==key:
            flag=1
            print ("Good job, ",player_name,"! You guessed my number in ",end="")
            print (trial+1," guesses!")
            break
        elif guess<key:
            print ("Your guess is too low.")
        elif guess>key:
            print ("Your guess is too high.")
    if flag==0:
        print ("Nope. The number I was thinking of was ",key)
     
def random_generate(a,b):
    return randint(a,b)

def check_validity_of_key(key):
    if key==-1:
        print ("Wrong_Choice_Of_Sack ...")        
        time.sleep(3)
        range_menu()
    else:
        start_game(key)
            
def range_menu():
    os.system('cls')
    print ("Select any one sack(range) from below to start the game...")
    print ("< 0-100 >  < 100-200 >  < 200-300 >  < 300-400 >  < 400-500 >")
    print ("< alpha >   < beta >    < charlie >   < delta >    < theta >")
    print ("Enter the Sack Name -> "),
    sack_name=input()
    sack_name=sack_name.lower()
    if sack_name=="alpha":
        key_generated=random_generate(0,100)
    elif sack_name=="beta":
        key_generated=random_generate(100,200)
    elif sack_name=="charlie":
        key_generated=random_generate(200,300)
    elif sack_name=="delta":
        key_generated=random_generate(300,400)
    elif sack_name=="theta":
        key_generated=random_generate(400,500)
    else:
        key_generated=-1
    load_program()
    check_validity_of_key(key_generated)
    #start_game(key_generated)

def help_menu():
    os.system('cls')
    print ("\t\tPress 1 -> Start the Game")
    print ("\t\tPress 2 -> Instructions")
    print ("\t\tPress 3 -> Developers")
    print ("\t\tPress 4 -> Exit")
    option=int(input("\tEnter your option -> "))
    if option==1:
        load_program()
        range_menu()
        #start_game(key)
    elif option==2:
        load_program()
        #instructions()
    elif option==3:
        load_program()
        #developers()
    elif option==4:
       load_program()       
       sys.exit()    
    else:
       print ("Wrong_Option")
       time.sleep(3)
       help_menu()

print (" _________________________________________________________________")
print ("|||||||||||||||||||||||GUESS_THE_NUMBER||||||||||||||||||||||||||||")
print ("|_________________________________________________________________|")
load_program()
help_menu()
        
    
