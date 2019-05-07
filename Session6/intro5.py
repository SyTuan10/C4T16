while True:
    password = input("Mat Khau Co Ca Chu Va So :  ")
    print(password)
    if password.isalpha():
        print("Nhap Lai")
    else:
        print("Password : ",password)
        break
print("Ban Da Nhap Dung")