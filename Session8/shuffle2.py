from random import shuffle,randint
list1 = ['Hello', 'The', 'World']

n = randint(0,len(list1)-1)
print("So Random : ", n)
a = list1[n]
k = list(list1[n])
shuffle(k)
print(k)

m = input("Nhap Tu Ban Doan : ")
if m == a:
    print("You Are Right")
else:
    print("You Are Wrong")