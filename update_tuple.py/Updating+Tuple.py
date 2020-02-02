
# coding: utf-8

# In[5]:

list = [( 1,2,3), ( 4,6,7) ]
add_list = 2

new = [tuple (j + add_list for j in sub) for sub in list]

print(str(new))


# In[ ]:



