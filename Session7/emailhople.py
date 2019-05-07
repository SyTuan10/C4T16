while True:
    email = input("Nhap Email : ")
    if len(email)<8:
        print("Chua Du So Ky Tu")
    elif email.isalpha():
        print("Email Must Have Number")
    elif email.isdigit():
        print("Email Must Have Alphabet")
    elif "@" not in email:
        print("Email Phai Co @")
    elif "." not in email:
        print("Email Phai Co .")
    else:
        break
print("Your Email : ",email)
print("You Have Done")