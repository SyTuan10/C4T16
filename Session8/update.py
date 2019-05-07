items = ['Sport', 'Lol', 'Drama']
new_item = input("New : ")
items.append(new_item)
items[3] = 'Spider Man'
print(*items, sep= ', ')
