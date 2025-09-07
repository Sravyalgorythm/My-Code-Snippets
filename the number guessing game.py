# -*- coding: utf-8 -*-
"""
Created on Mon Sep  1 20:00:32 2025

@author: Usha
"""
import random 
print('THIS IS THE GUESSING GAME')
print('You have to guess which number the computer chose!')
user_choice=int(input('guess a number from 1 to 10:  '))
nums=[1,2,3,4,5,6,7,8,9,10]
guess=1
comp_choice=random.choice(nums)
while user_choice!=comp_choice:
    if user_choice>comp_choice:
        print('lower!')
    elif user_choice<comp_choice:
        print('higher!')
    user_choice=int(input('Try again:'))
    guess+=1
if user_choice==comp_choice:
    print(f'You guessed it! the number is {comp_choice}')
    print(f'It took you {guess} guesses!')