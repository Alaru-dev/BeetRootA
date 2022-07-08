#The Guessing Game.
import random
print('Lets play Guessing Game!')
input_num = input('Please guess what number was generated (between 1 and 10): ')
if input_num.isdigit() == True:

    if int(input_num) >= 1 and int(input_num) <= 10:

        if random.randint(1, 10) == int(input_num):
            print('You win!')
        else:
            print('You lost')

    else:
        print('You number out of range!!!')

else:
    print('Please write a number!')