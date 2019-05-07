from random import randint
countPoint = 0
countNumber = 0
n = int(input("Ban muon choi bao nhieu lan: "))
while True:
    a = randint(0,15)
    b = randint(0,5)
    x = randint(-1,1)
    c = a + b + x
    
    print("Lan choi thu",countNumber+1)
    print(c ,"=", a ,"+", b)
    
    r = input("Doan ket qua (T/F): ").upper()
    if r == "T":
        if x == 0:
            countPoint += 1
            print("Ban Dung")
        else:
            print("Ban Sai")
            print("Diem cua ban la:",countPoint)
            break
    elif r == "F":
        if x != 0:
            countPoint += 1
            print("Ban Dung")
        else:
            print("Ban Sai")
            print("Diem cua ban la:",countPoint)
            break
    else:
        print("Choi lai")
    if countNumber < n-1:
        countNumber += 1
    else:
        print("Het",n, "lan choi")
        print("Diem cua ban la:",countPoint)
        break

