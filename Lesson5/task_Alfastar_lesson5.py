users = [                       #here first we need to tarnsform all data to normal list format
    [321, 'Hello', 200, 1],     #[id, name, balance, level]
    [2, 'Harry Potter', 101, 9],
    [4, 'Nik', 34000, 1000],
    [51, 'Logan', 100, 10],
    [10000004, 'Lanos', 13500, 23],
    [23, 'CyberGiant', 13501, 23],
    [1, 'Abram']
    ]
for user in users:
    if len(user) == 4:
        if user[-1] < 10 and user[-2] <= 100:
            print(f'{user[0:2]} звичайний ігрок')
        elif user[-1] >= 10 and user[-1] < 23 and user [-2] <= 13500:
            print(f'{user[0:2]} звичайний ігрок')
        elif user[-1] >= 23 and user[-2] > 13500:
            print(f'{user[0:2]} звичайний ігрок')
        else:
            print(f'{user[0:2]} - чітер !!!')
    else:
        print(f'Запис {user} некоректний!')