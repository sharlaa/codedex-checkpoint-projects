import random

print('===================')
print('Rock Paper Scissors')
print('===================')

player = int(input(""" 
1) ✊  
2) ✋ 
3) ✌️ 
Pick a number: """))

computer = random.randint(1, 3)

if player == 1 and computer == 2:
    answer = 'The player lost!'
elif player == 1 and computer == 3:
    answer = 'The player won!'
elif player == 2 and computer == 1:
    answer = 'The player won!'
elif player == 2 and computer == 3:
    answer = 'The player lost!'
elif player == 3 and computer == 1:
    answer = 'The player lost!'
elif player == 3 and computer == 2:
    answer = 'The player won!'
else:
    answer = "It's a tie!"

print('You choose:', player)
print('Computer choose:', computer)
print(answer)






