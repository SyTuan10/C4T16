while True:
    name = input("Ho va Ten : ")
    if name.isalpha():
        print("Name : ",name)
        break
    else:
        print("Name has number")
