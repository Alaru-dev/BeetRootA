print("<<< String Manipulation >>>") #name

def str_manipulation(): #funct for manipulation
    get_str = input('Write a text: ')
    if len(get_str) >= 2:
        print(get_str[0:2]+get_str[-2:])
    elif len(get_str) < 2:
        print("Empty String")


input_start=input("Start manipulation (Y-yes/N-no): ") #starting command

if input_start.lower() == "y":
    str_manipulation()
elif input_start.lower() == "n":
    print("Have a nice day ;)")
else:
    print("Incorrect command!")

continue_man = input("Are you want to continue (Y-yes/N-no):") #continue command

if continue_man.lower() == "y":
    str_manipulation()
elif continue_man.lower() == 'n':
    print("Have a nice day ;)")
else:
    print("Incorrect command!")

