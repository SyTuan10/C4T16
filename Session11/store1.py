store={
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
    'ACER': 25,
}
prize={
    'HP': 600,
    'DELL': 650,
    'MACBOOK': 12000,
    'ASUS': 400,
    'ACER': 350,
}
m= 0
for i in store.keys():
    for k in range(1):
        n= store[i]*prize[i]
        print('Tổng giá của ', i, 'là: ', n)
        m += n
print('Tổng giá trị toàn bộ các máy trong kho: ',m)
