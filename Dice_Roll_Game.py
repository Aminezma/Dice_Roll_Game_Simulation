import random

# Drawing the 6 Dice Sides

dices = [ '''----------------------
|                    |             
|         .          |
|                    |
----------------------      '''

,

 '''----------------------
| .                   |             
|                     |
|                   . |
----------------------      '''
,
 '''----------------------
| .                   |             
|         .           |
|                   . |
----------------------      '''

,

'''----------------------
| .                 . |             
|                     |
| .                 . |
----------------------      '''

,

'''----------------------
| .                 . |             
|          .          |
| .                 . |
----------------------      '''
,

'''----------------------
| .        .        . |             
|                     |
| .        .        . |
----------------------      '''

]
# PLayers in the Game

print('\n********Roll the Dice**********\n')



human_player = input('>')

while True:

    if human_player == 'Roll':
        
        human_luck = random.choice(dices)
        
        print('\n*****Your Roll******\n')

        print(human_luck)
        
        break
        
    elif human_player != 'Roll':
        
        print('Please Roll the Dice!!!\n')  
        

computer_luck = random.choice(dices)

print('\n*****Computer Rolls******\n')

print(computer_luck)
    
# Tie Game
    
print('\nIt is a Tie') if computer_luck == dices[0] and human_luck == dices[0] else print('')
print('\nIt is a Tie') if computer_luck == dices[1] and human_luck == dices[1] else print('')
print('\nIt is a Tie') if computer_luck == dices[2] and human_luck == dices[2] else print('')
print('\nIt is a Tie') if computer_luck == dices[3] and human_luck == dices[3] else print('')
print('\nIt is a Tie') if computer_luck == dices[4] and human_luck == dices[4] else print('')
print('\nIt is a Tie') if computer_luck == dices[5] and human_luck == dices[5] else print('')


# Human Win
  
print('\nYou Win!!!!') if computer_luck == dices[0] and human_luck == dices[1] or human_luck == dices[2] or human_luck == dices[3] or human_luck == dices[4] or human_luck == dices[5] else print('')
print('\nYou Win!!!!') if computer_luck == dices[1] and human_luck == dices[2] or human_luck == dices[3] or human_luck == dices[4] or human_luck == dices[5] else print('')
print('\nYou Win!!!!') if computer_luck == dices[2] and human_luck == dices[3] or human_luck == dices[4] or human_luck == dices[5] else print('')
print('\nYou Win!!!!') if computer_luck == dices[3] and human_luck == dices[4] or human_luck == dices[5] else print('')
print('\nYou Win!!!!') if computer_luck == dices[4] and human_luck == dices[5] else print('')


# Computer Win
  
print('\nComputer Wins!!!!') if human_luck == dices[0] and computer_luck == dices[1] or computer_luck == dices[2] or computer_luck == dices[3] or computer_luck == dices[4] or computer_luck == dices[5] else print('')
print('\nComputer Wins!!!!') if human_luck == dices[1] and computer_luck == dices[2] or computer_luck == dices[3] or computer_luck == dices[4] or computer_luck == dices[5] else print('')
print('\nComputer Wins!!!!') if human_luck == dices[2] and computer_luck == dices[3] or computer_luck == dices[4] or computer_luck == dices[5] else print('')
print('\nComputer Wins!!!!') if human_luck == dices[3] and computer_luck == dices[4] or computer_luck == dices[5] else print('')
print('\nComputer Wins!!!!') if human_luck == dices[4] and computer_luck == dices[5] else print('')

