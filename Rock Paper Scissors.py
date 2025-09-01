# A round of rock paper scissors!

import random

choices=['rock','paper','scissors']
print('ROCK, PAPER, SCISSORS, SHOOT!')

your_choice=input('What do you choose?: ').lower()
comp_choice=random.choice(choices)
print(f'The computer chose: {comp_choice}')

if comp_choice==your_choice:
    print("It is a tie!")
elif ((comp_choice=='rock' and your_choice=='paper') or 
     (comp_choice=='paper'and your_choice=='scissors') or 
     (comp_choice=='scissors' and your_choice=='rock')):
    print('YOU WIN!')
elif your_choice not in choices:
    print('oops that is not a valid choice')
else:
    print('Computer wins!')