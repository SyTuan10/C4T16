while True:
    crud = ('C','R','U','D')
    n = input("Chon : ")
    sothich =['lol', 'pubg', 'USUK']

    if n == "C":
        soThichMoi = input("nhap so thich : ")
        sothich.append(soThichMoi)
        print(sothich)
    elif n == "R":
        for i, sothich in enumerate(sothich):
            print(i, sothich)
    elif n == "U":
        m = int(input("vi tri ban muon thay doi : "))
        sothich[m] = input("Ten ban muon doi : ")
        print(sothich)
    elif n == "D":
        k = int(input("vi tri ban muon xoa : "))
        sothich.pop(k)
        print(sothich)
