# -*- coding: utf-8 -*-
"""
Created on Wed May 13 13:46:31 2026

@author: Sravya
"""
import pandas as pd

movies=[
        {"Movie": "Rise of the planet of the apes","Released": "2001","Genre": "Sci-fi"},
        {"Movie": "John Wick","Released": "2014","Genre": "Action"},
        {"Movie": "Mean Girls","Released": "2004","Genre": "Comedy"},
        {"Movie": "Accepted","Released": "2006","Genre": "Comedy"},
        {"Movie": "The Notebook", "Released": "2004","Genre": "Romance"}
        ]
movie_df=pd.DataFrame(movies)
print(movie_df)

choice=input("What Genre are you feeling? - ")
print("Your rec for tonight - ")
count=1
for i,r in movie_df.iterrows():
    if r["Genre"].lower() == choice.lower():
        print(f"{count}) {r['Movie']}")
        print("Release date - ",r["Released"])
        count=count+1
if count!=1:
    print("Enjoy!")
else:
    print("Oops- Looks like your Genre isnt here right now.")
       