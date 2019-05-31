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

for i,Skill1 in enumerate(Skill1.keys()):
    print(i+1,Skill1)