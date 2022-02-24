# Tayyip Güney 20.02.2022

# Number Guessing Game
# General Information:
# I want to play a game which I can guess a number. 
# The computer chooses a number in the range I chose. 
# So that I can try to find the correct number which was selected by computer.

# Acceptance Criteria:
# * Computer must randomly pick an integer from user selected a range, i.e., from A to B, where A and B belong to Integer. 
# * Your program should prompt the user for guesses if the user guesses incorrectly, it should print whether the guess is too high or too low. 
# * If the user guesses correctly, the program should print total time and total number of guesses. 
# * You must import some required modules or packages You can assume that the user will enter valid input.

from datetime import datetime
from random import randrange


start_num=int(input("starting number : "))
end_num=int(input("ending number   : "))

rand_num=randrange(start_num,end_num)

count=0
a = datetime.now()
print("\nTime has begun")
while True:
    guess=int(input("\nenter your guess : "))
    count+=1
    if (guess>rand_num):
        print("your guess is HIGHER than the number")
        continue
    elif (guess<rand_num):
        print("your guess is LOWER than the number")
        continue
    else:
        b=datetime.now()
        break
dur=""    
tim=int((b - a).seconds)
if tim>60:
       mint=tim//60
       sec=tim%60
       dur=str(mint)+" minutes "+str(sec)+" seconds"
else:   
    dur=str(tim)+" seconds"
print(f"\nCongratulations. {rand_num} is the correct number",
      f"\nnumber of attempts : {count}",
      f"\nduration of attempts : {dur}"
      )
