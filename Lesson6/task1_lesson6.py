#The greatest number
import random
i = 1
random_list = []
while i <= 10:
        random_list.append(random.randint(0,100))
        i += 1
print(max(random_list))
