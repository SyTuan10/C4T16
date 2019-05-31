from random import uniform
Skill1={
'Name': 'Tackle',
'Minimum level': 1,
'Damage': 5,
'Hit rate': 0.3,
}
Skill2={
'Name': 'Quick attack',
'Minimum level': 2,
'Damage': 3,
'Hit rate': 0.5,
}
Skill3={
'Name': 'Strong Kick',
'Minimum level': 4,
'Damage': 9,
'Hit rate': 0.2,
}

char= [Skill1, Skill2, Skill3]
m= uniform(0.0, 1.0)
print('''- You are being ganked by opponent jungler Kha'zix
- Your skills are available:''')
for i in range(3):
    print(i+1, char[i]['Name'])
while True:
    n= int(input('Choose your skill: '))
    if n<3:
        print('Skill is available')
        print('Hit rate: ', m)
        if m < Skill1['Hit rate']:
            print('Skill damage: ', char[n-1]['Damage'])
        else:
            print('Missed')
        break
    else:
        print("Skill isn't available")


# while True:
#     n= int(input('Choose your skill: '))
#     if n== 1:
#         print('Skill is available')
#         print('Skill damage: ', Skill1['Damage'])
#         break
#     elif n== 2:
#         print('Skill is available')
#         print('Skill damage: ', Skill2['Damage'])
#         break
#     else:
#         print("Skill isn't available")
