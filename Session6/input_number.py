while True:
    txt = input("Enter a number")
    print(txt)
    if txt.isdigit():
        print("A number")
        break
    else:
        print("Not a number")

print(2019 - int(txt))