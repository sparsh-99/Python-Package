#!/usr/bin/env python
# coding: utf-8

# # Use the Shirt Class

class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price
    
    def change_price(self, new_price):
    
        self.price = new_price
        
    def discount(self, discount):

        return self.price * (1 - discount)


Shirt('red', 'S','long-sleeve',25)
shirt_one = Shirt('red', 'S','long-sleeve',25)


print(shirt_one.price)
shirt_one.change_price(10)
print(shirt_one.price)
print(shirt_one.discount(.12))


shirt_two = Shirt('orange','L','short-sleeve',10)


total = shirt_one.price + shirt_two.price


total_discount = shirt_one.discount(.14) + shirt_two.discount(.06)




# Unit tests to check your solution
from tests import run_tests

run_tests(shirt_one, shirt_two, total, total_discount)







