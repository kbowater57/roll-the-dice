# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:00:14 2019

@author: kbowa
This project will produce a text interface for a generator for n-sided dice rolls
"""
import random
#print ("Hello there! I am Dicey. How many sides would you like your dice to be?")
#sides = eval(input("Hello there! I am Dicey. How many sides would you like your dice to have? \n"))
sides_untested = input("Hello there! I am Dicey. How many sides would you like your dice to have? \n")
try: 
    sides = eval(sides_untested)
    print("Your " + str(sides) + "-sided dice rolled a " + str(random.randrange(1,sides)) + " .")
    
except (ValueError,NameError):
    print("A dice can't have " + sides_untested + " sides!")
#print("Your " + str(sides) + "-sided dice rolled a " + str(random.randrange(1,sides)) + " .")