items = ['Sport', 'Lol', 'Drama']
new_item = input("New : ")
items.append(new_item)
items[3] = 'Spider Man'
print(*items, sep= ', ')
print(str.upper(items[0]))
print(str.upper(items[1]))
print(str.upper(items[2]))
print(str.upper(items[3]))