store={
    'HP': 20,
    'DELL': 50,
    'MACBOOK': 12,
    'ASUS': 30,
    'ACER': 25,
}
n= 0
# print('Số lượng MACBOOK có trong kho: ',store['MACBOOK'])

# n= str.upper(input('Hãng máy tính: '))
# print('Số máy tính có trong kho là: ',store[n])

# store['TOSHIBA'] = 10
# store['DELL'] = 60
# store['MACBOOK'] = 2
store['FUJITSU'] = 15

for i in store.keys():
    n += store[i]
print('Số máy có trong kho: ',n)

