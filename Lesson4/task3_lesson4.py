# The math quiz program

input_start = input("Start math quiz program (Y/N): ")
if input_start.lower() == "y":
    import random
    int_1 = random.randint(0, 50)
    int_2 = random.randint(0, 10)
    addition = (f'{int_1 + int_2}')
    subtraction = (f'{int_1 - int_2}')
    division = (f'{int_1 / int_2}')
    multiplication = (f'{int_1 * int_2}')
    operator = random.choice(['+','-','/','*'])
    input_answer = input(f'Write a right answer for math expression: "{int_1}{operator}{int_2}": ')
    if input_answer == addition or input_answer == subtraction or input_answer == division or input_answer == multiplication:
        print('All right! Good job!')
    else:
        print('Answer isn`t correct! Try again!')

elif input_start.lower() == 'n':
    print("Bye! Have a nice day!")
else:
    print("Incorrect command!")

