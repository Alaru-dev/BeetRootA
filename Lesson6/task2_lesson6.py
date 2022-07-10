#Exclusive common numbers.
import random

first_list = []
second_list = []
i = 1
while i <= 10:  #add random numbers in 2 lists
        first_list.append(random.randint(1, 10))
        second_list.append(random.randint(1, 10))
        i += 1

uni_list = list(set(first_list+second_list)) #use set to make uniq numbers in one list

print(uni_list)
