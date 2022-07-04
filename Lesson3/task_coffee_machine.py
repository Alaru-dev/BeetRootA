zerna = int(input("Скільки кавових зерен використати?(від 0 до 5): "))
zuker = int(input("Скільки кубіків цукру додати? (0 або більше): "))
milk = int(input("Дадати молока? (так - 1; ні - 0): "))

if zerna == 0:
    print("\nЦей напій не є кавою.")
elif zerna == 1 or zerna == 2:
    print("\nСлабка кава.")
elif zerna == 3 or zerna == 4:
    print("\nМіцна кава.")
elif zerna >= 5:
    print("\nДуже міцна кава.")
else:
    print('\nКавові зерна - Quantity error!!!')

if zuker == 0:
    print('Кава без цукру, гарний вибір.')
elif zuker > 0:
    print(f'Додаю цукор за смаком - {zuker} од. ')
else:
    print('Цукор - Quantity error!!!')

if milk == 0 and zuker >= 0:
    print('Роблю амерікано. Смачного!')
elif milk == 1 and zuker >= 0:
    print('Роблю лате. Смачного!')
else:
    print('Молоко - Quantity error!!!')


