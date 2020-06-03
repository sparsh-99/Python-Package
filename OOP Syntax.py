#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
        
    def change_price(self,new_price):
        self.price = new_price
        
    def discount(self, discount):
        return self.price * (1-discount)


# In[5]:


Shirt('red','S','Short',25)


# In[8]:


new_shirt = Shirt('red','S','Short',25)


# In[13]:


print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)


# In[11]:


new_shirt.change_price(10)
print(new_shirt.price)


# In[14]:


print(new_shirt.discount(.2))


# In[15]:


tshirt_collection=[]
shirt_one = Shirt('red','S','Short',25)
shirt_two = Shirt('orange','L','Sleeveless',15)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)

for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].price)


# In[ ]:




