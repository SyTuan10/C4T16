quan = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
danso = ['150300', '247100', '333300', '266800', '420900', '318000']
dientich = ['117.43', '9.224', '43.35', '12.04', '99.6', '10.09']

count = 0 
for i in range(6):
    matDoDanCu = float(danso[i])/float(dientich[i])
    count += matDoDanCu
    print("Mat Do Dan Cu Theo Thu Tu : ", matDoDanCu)
print("Mat Do dan cu TB : ",count/6 )


# n = max(danso)
# print("Dan so lon nhat : ", n)
# m = danso.index(n)
# print(m)
# print("Quan co dan so max : ", quan[m])

# a = min(danso)
# print("Dan so it nhat : ", a)
# b = danso.index(a)
# print(b)
# print("Quan co dan so min : ", quan[b])
# for i in range(x):