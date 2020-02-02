
# coding: utf-8

# In[1]:

import string
import random

def password (userInput): 
    characters = [random.choice(string.punctuation) for character in range (userInput)]
    Lowercase = [random.choice (string.ascii_lowercase) for lower in range (userInput)]
    Uppercase = [random.choice (string.ascii_uppercase) for upper in range (userInput)]
    Numbers = [random.choice (string.digits) for number in range (userInput)]
    Password = ''.join(characters + Lowercase + Uppercase + Numbers)
    Password = ''. join(random.choice (Password) for value in range (userInput)) 
    return Password

Question = int(input ('Enter your password lenght: '))
Answer =password(Question)
Answer


# In[ ]:



