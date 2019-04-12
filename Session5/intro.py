n = input("enter your yob")
m = 2019 - int(n)
print (m)

if m<10:
    print("Baby")
elif m<18:
    print("Teenager")
else:
    print("Adult")