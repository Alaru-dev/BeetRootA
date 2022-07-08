print("<<< String Manipulation >>>")
get_str = input('Write a text: ')

def str_manipulation(get_str):
    if len(get_str) >= 2:
        print(get_str[0:2]+get_str[-2:])
    elif len(get_str) < 2:
        print("Empty String")

str_manipulation(get_str)

