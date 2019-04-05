# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:00:14 2019

@author: kbowa
This project will produce a text interface for a generator for n-sided dice rolls
"""
import random
#print ("Hello there! I am Dicey. How many sides would you like your dice to be?")
sides = eval(input("Hello there! I am Dicey. How many sides would you like your dice to have? \n"))
print("Your " + str(sides) + "-sided dice rolled a " + str(random.randrange(1,sides)) + " .")

