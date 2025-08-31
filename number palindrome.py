# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 18:04:11 2025

@author: Usha
"""

    
#Number Palindrome Program

n=int(input('Enter a positive integer number: '))
k=str(n) 
pali_check= k[::-1]    #reversing the string

print(f'{pali_check}, is the reversed number')
if pali_check==k:
    print("Palindrome!")
else:
    print('Not a palindrome!')
