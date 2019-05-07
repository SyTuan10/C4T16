account = input("Ten Tai Khoan : ")
password = input("Mat Khau : ")
while True:
    password1 = input("Nhap lai Mat Khau : ")
    if password != password1:
        print("Nhap Lai")
    elif password == password1:
        print("Xong")
        break
print("Account : ",account)
print("Password : ",password)