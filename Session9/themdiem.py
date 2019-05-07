diem = [50, 70, 80, 60, 90, 100]
diemmoi = int(input("Nhap Diem Moi : "))
diem.append(diemmoi)
print("Diem : ",diem)
diem.sort(reverse=True)
print(diem)

for i, diem in enumerate(diem):
    print(i + 1 , diem)
# for i in range(5):
#     print(i+1,diem)