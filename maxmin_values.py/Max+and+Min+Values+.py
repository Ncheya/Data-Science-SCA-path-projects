
# coding: utf-8

# In[4]:

list = []
num = int(input ("number of values on the list: "))

for x in range(1, num + 1):
    numbers = int(input("enter %d number : " %x))
    list.append(numbers)
    
print("Highest value in the list is : ", max(list))
print("Lowest value in the list is : ", min(list))


# In[ ]:



