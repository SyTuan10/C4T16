while True:
    password = input("Mat Khau Co Ca Chu Va So :  ")
    print(password)
    if password.isalpha():
        print("Nhap Lai")
    elif len(password) < 8:
        print("MK chua co 8 ky tu")
    else:
        print("Password : ",password)
        break
print("Ban Da Nhap Dung")