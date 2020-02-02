
# coding: utf-8

# In[1]:

import random

def isNum (s:str)->bool:
    try:
        int(s)
        return True
    except: 
        return False
    
randomNumber = random.randint(1, 100)

guess = input("Guess a number between 1 to 100: ")

while guess != str(randomNumber):
    if isNum(guess):
        print("Sorry, your guess is too " + ("low" if int(guess)< randomNumber else "high"))
        print(randomNumber)
    else:
            print("Invalid Input")
            
            guess = input("Try again: ")
        
    print("Correct!")
    Break
    


# In[ ]:




# In[ ]:



