# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:00:14 2019

@author: kbowa
This project will produce a text interface for a generator for m n-sided dice
rolls, checking for sensible user input.
"""
import random

all_done = 0
print("Hello there! I am Dicey.")
while all_done == 0:
    
    sides_untested = input("How many sides would you like your dice to have? \n")
    
    try: 
        sides = eval(sides_untested)
        print("Your " + str(sides) + "-sided dice rolled a " + str(random.randrange(1,sides)) + " .")
        user_satisfied = str(input("Would you like to roll any more dice? Type y or n.\n"))
        if user_satisfied == "y":
            print("Okay! Coming right up.")
        elif user_satisfied == "n":
            print("Thank you for using my services!")
            all_done = 1
        elif user_satisfied == "n.":
            print("You are a true coder.Thank you for using my services!")
            all_done = 1
        else:
            print("What kind of an answer is that?!")
            all_done = 1
    except (ValueError,NameError):
        print("A dice can't have " + sides_untested + " sides! Try again.")
