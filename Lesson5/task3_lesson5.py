#Words combination
import random

input_str = input('Please write a text: ')
i = 1
while i < 6:
    print(''.join(random.choices(input_str, weights=None, k=len(input_str)))) #Form 5 random chars, after join in one str
    i += 1
