# <<< The valid phone number program >>>
input_ph_num = input('Write phone number(just numbers): ')

if input_ph_num.isdigit() == True :
    print('Check digits - Consists only numbers')
    if len(input_ph_num) == 10:
        print("Check length - Consists 10 chars")
        print("Your phone number is correct!")
    else:
        print('Check length - wrong quantity!')
else:
    print("Check digits - Please write just numbers!")