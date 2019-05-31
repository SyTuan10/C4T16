map = {
    'x':4,
    'y':4,
}
P = {
    "x":1,
    "y":0,
}
K= {
    'x':0,
    'y':2,
}
E={
    'x':3,
    'y':3,
}
key_storage = 0
while True:
    for y in range(map['y']):
        for x in range(map['x']):
            if P['x']== x and P['y']== y:
                print('P',end=" ")
            elif K['x']== x and K['y']== y:
                if key_storage ==0:
                    print('K',end=" ")
                else:
                    print('-',end=" ")
            elif E['x']== x and E['y']== y:
                print('E',end=" ")
            else:
                print("-",end=" ")
        print('')
    # print(''*30)
    if P['x']== E['x'] and P['y']== E['y']:
        if key_storage == 0:
            print("You must have key to exit")
        else:
            print('Congrats, you’ve just escaped the dungeon')
            break
    n= input('Your step: ').upper()
    dx=0
    dy=0
    if n == 'W':
        dy = -1
    elif n== 'S':
        dy = 1
    elif n== 'D':
        dx = 1
    elif n=="A":
        dx = -1
    else:
        print("Nhap lai")
    # Cách di chuyển P
    if (P['x']+dx) in range(map['x'])and (P['y']+dy) in range(map['y']):
        P['x']+= dx
        P['y']+= dy  
    if P['x']== K['x']and P['y']== K['y']:
        key_storage += 1
        print('You’ve just picked up a key!!!')
        
    