import random

def main():
  dice_rolls = int(input('\nHow many dice you want to roll : '))
  dice_size = int(input('\nHow many sides a dice have : '))
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,dice_size)
    dice_sum += roll 
    if roll == 1:
      print(f'You rolled a {roll} ! Critical Failure !')
    elif roll ==dice_size:  
      print(f'You rolled a {roll} ! Criticial Success !')
    else:
      print(f'You rolled a {roll}')
  print(f'Dice sum = {dice_sum}')

if __name__== "__main__":
  main()