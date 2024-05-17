#!/usr/bin/env python
# coding: utf-8
#Define the menu of restaurant
menu = {
    "pizza" : 40,
    "pasta" : 50,
    "burger": 60,
    "salad" : 70,
    "coffe" : 80,
}

#Greet
print ("Welcome to our Python Restaurant")
print ("pizza : Rs40\npasta : Rs50\nburger : Rs60\nsalad : Rs70\ncoffe : Rs80\n")

# In[22]:


order_total = 0 
#80 + 70 = 150/- ---Example---

item_1 = input("Enter the name of item you want to order ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 50 
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} not available yet ")

another_item = input("Do you want to add another item ? (YES/NO)")
if another_item == "YES":
          item_2 = input("Enter the name of second item = ")
          if item_2 in menu:
              order_total += menu[item_2]
              print(f"item {item_2} has been added to your order")
          else:
              print("Ordered item {item_2} is not available yet")
                
print(f"The total amount of items to pay is {order_total}")


# In[21]:





# In[ ]:




